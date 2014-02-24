'''
Created on Nov 21, 2012

@author: dawood
'''
import logging
from unittest import TestLoader
from agilityshell import agility
import os
import sys
from core.pyworx import pythonpath
COMPONENT_NAME = 'fieldtests'
import logger
logger = logger.getLogger(COMPONENT_NAME)

class TestSuiteDesigner(object):
    def __init__(self, agility):
        self._agility = agility
        self._testloader = TestLoader()
        
    def discover(self, startpath='', pattern='test*.py', rootpath=None):
        startpath = startpath or os.path.join(agility.cfg.path.pluginsdir, 'fieldtests', 'testcases')
        startpath = os.path.realpath(os.path.abspath(startpath))
        if rootpath: pythonpath.addPath(rootpath)
        logger.info('Discovering test cases in path [%s], root path [%s]', startpath, rootpath or '')
        suite = self._testloader.discover(startpath, pattern=pattern, top_level_dir=rootpath)
        return suite
    
    