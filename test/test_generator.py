'''
Description:

@author: cgerber
'''
import os
import sys
import unittest
import logging
import base64
import xml.dom.minidom
import pycurl

from pycurl import Curl
from io import BytesIO
from os import path
from shutil import copyfile

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import logger

logger.configRootLogger('test_generate_wadl', '.', 'unittest.log', logging.DEBUG, console=True) 

from logger import logger
from core.config.configuration import AgilityShellConfig
from core.restclient.generator.generate_client_methods import Application, generate_python_module, update_file_if_changed

WADL_FILENAME = 'agility.wadl'
GENERATOR_PATH = 'core/restclient/generator'
AGILITY_PATH = 'core/agility'

class GeneratorTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.buffer = BytesIO()
        self.conf = AgilityShellConfig(path="agilityshell.cfg") 
        self.url = "https://%s:%s/agility/api/%s/application.wadl?detail=true" % (self.conf.get(section='main', option='host'), self.conf.get(section='main', option='port'), self.conf.get(section='apiversion', option='version'))

        self.curl = Curl()
        self.curl.setopt(pycurl.URL, self.url)
        self.curl.setopt(pycurl.WRITEDATA, self.buffer) 
        self.curl.setopt(pycurl.VERBOSE, True)
        self.curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        self.curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        self.curl.setopt(pycurl.HTTPHEADER, ["Accept:application/vnd.sun.wadl+xml", 
                                             "Authorization:Basic %s" % base64.encodebytes(bytes("%s:%s" % (self.conf.get(section='main', option='username'), self.conf.get(section='main', option='password')), "utf-8")).decode("utf-8")])
        
        self.cwd = os.getcwd()
        self.wadlFile = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), WADL_FILENAME), "wb+")
        self.generatorPath = os.path.join(self.cwd, GENERATOR_PATH)
        
        self.generatorApiPath = os.path.join(self.generatorPath, self.conf.get(section='apiversion', option='version').replace('.', '_'))
        if not os.path.exists(self.generatorApiPath):
            os.makedirs(self.generatorApiPath) 
        
        self.generatorMethodsPath = os.path.join(self.generatorApiPath, 'methods.py')
        
        self.agilityPath = os.path.join(os.path.join(self.cwd, AGILITY_PATH), self.conf.get(section='apiversion', option='version').replace('.', '_'))
        if not os.path.exists(self.agilityPath):
            os.makedirs(self.agilityPath) 
            
        agilityInitPath = os.path.join(self.agilityPath, '__init__.py')
        if not os.path.exists(agilityInitPath):
            self.agilityInitFile = open(agilityInitPath, "wb+")
            self.agilityInitFile.close()
            
        self.agilityMethodsPath = os.path.join(self.agilityPath, 'methods.py')     
            
        self.modelPath = os.path.join(self.agilityPath, 'agilitymodel')
        if not os.path.exists(self.modelPath):
            os.makedirs(self.modelPath) 
            
        modelInitPath = os.path.join(self.modelPath, '__init__.py')
        if not os.path.exists(modelInitPath):
            self.modelInitFile = open(modelInitPath, "wb+")
            self.modelInitFile.close()
        
    def tearDown(self):
        os.chdir(self.cwd)
        self.curl.close()
        self.wadlFile.close()
        
    def testGenerator(self):
        #Generate WADL
        self.curl.perform() 
        self.assertEquals(self.curl.getinfo(pycurl.RESPONSE_CODE), 200)
        self.wadlFile.write(self.buffer.getvalue())
        
        #Generate Methods
        self.wadlFile.seek(0)
        doc = xml.dom.minidom.parse(self.wadlFile)
        os.chdir(self.generatorPath)
        content = generate_python_module(Application(doc.documentElement))
        update_file_if_changed(self.generatorMethodsPath,content)
        copyfile(self.generatorMethodsPath, self.agilityMethodsPath)
        
        #Generate Model
        os.chdir(self.cwd)
        from core.restclient.generator.ModelFromHTMLSpecs import parseHTMLSpecs
        os.chdir(self.agilityPath)
        parseHTMLSpecs()
        
if __name__ == "__main__":
    unittest.main()        
        