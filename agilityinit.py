'''
Created on Nov 16, 2012

@author: dawood
'''
####################### <BEGIN> KEEP THE FOLLOWING INIT CODE ON TOP OF EVERYTHING ELSE ###########################
import os, sys
#the following trick can't be done from the agilityshell.py file, since the main entry point with __name__ == '__main__' might not have a __file__ attribute, depending on the Python implementation for the underlying platform
SHELL_ROOT_DIR = os.path.dirname(sys.modules[__name__].__file__)
import logging
from logger import configRootLogger
configRootLogger('agilityshell', os.path.join(SHELL_ROOT_DIR, 'logs'), 'agilityshell.log', logging.DEBUG, console=True) 
####################### <END> KEEP THE FOLLOWING INIT CODE ON TOP OF EVERYTHING ELSE ###########################
from logger import logger
from core.pyworx import pythonpath
from core.pyworx.partialfunc import partially
from core.config.configuration import AgilityShellConfig

srcfolders = ['.', SHELL_ROOT_DIR]
pythonpath.addPaths(srcfolders, basedir=SHELL_ROOT_DIR)
from core.base.enum import Enum
from core.proxy.serviceproxy import ServiceProxy
from core.proxy.hook import Hook

from core.plugin import loadPlugins, reloadPluginFeature
from shellutils.utils import Tools
from core.restclient.connection import RESTConnection
from core.restclient.search.query import AgilityQuery
from core import universal
from core import agility as client
from core.agility.common.service import Endpoint

import inspect

BOOLEAN = {'True' : True, 'False' : False}

def getConfiguration(path=None):
    path = path or os.path.join(SHELL_ROOT_DIR, 'agilityshell.cfg')
    configuration = AgilityShellConfig(path=path)
    return configuration

def configure(config=None):
    config = config or getConfiguration()
    return config

def getConnection(config):
    from core.restclient.connection import RESTConnection
    conn = RESTConnection(auth=config.main_auth, host=config.main_host, username=config.main_username, password=config.main_password, systemversion=config.main_systemversion, version=config.apiversion_version, use_cookies=config.main_use_cookies, reauthenticate=config.main_reauthenticate, ssl_context_unverified=config.main_ssl_context_unverified, ssl_cacert_location=config.main_ssl_cacert_location)
    return conn

def query(**kwargs):
    return AgilityQuery(**kwargs)

class Agility(object):
    def __init__(self, conn, configuration, assetName='ROOT', logger=None):
        self.cfg = Hook()
        self.cfg.conn = conn
        self._loadServices(configuration)
        self._initLogger(configuration, _logger=logger)
        self._initDirs()
        self.tools = Tools()

    def _loadServices(self, configuration):
        #Note: In a shell context, apiversion is set globally before instantiating the Agility object
        _client = client.getClient()
        attrnames = dir(_client)
        self._services = [attrname for attrname in attrnames if isinstance(getattr(_client, attrname), type) and issubclass(getattr(_client, attrname), Endpoint)]
        if 'Endpoint' in self._services :
            self._services.remove('Endpoint') #@todo: use decorators and tag services with a marker attribute to avoid using dir(module) and receiving the Base Class as an attribute that meets the criteria: isinstance(Base Class)
        self._assetNames = [assetName.title() for assetName in self._services]
        prefetch = configuration.get('main', 'prefetch')
        [object.__setattr__(self, serviceName, ServiceProxy(self.cfg.conn, serviceName.title(), prefetch)) for serviceName in self._services]
    
    def _addServiceMethod(self, func, alias=None):
        '''
        transplant utility functions into the object graph, function must implement the signature: func(agility, assetName, *args, **kwargs)
        ''' 
        alias = alias or func.__name__
        for serviceName in self._services:
            serviceMethod = partially(func, self, serviceName)
            setattr(getattr(self, serviceName), alias, serviceMethod)
        return self
    
    def _addHTTPExceptionWrapper(self, HTTPResponseCode, exceptionClass, message=''):
        '''
        Register an (external) exception class with the shell. Instances of this exception would be raised when the corresponding HTTPResponseCode is returned from the Server
        '''
        self.cfg.conn.http_exception_hooks[int(HTTPResponseCode)] = (exceptionClass, message)
    
    def _initLogger(self, configuration, _logger):
        if _logger :
            self.cfg.logger = _logger
        else :    
            self.cfg.logger = logger
            
        level = Enum(**dict(CRITICAL = logging.CRITICAL,
                    FATAL = logging.CRITICAL,
                    ERROR = logging.ERROR,
                    WARNING = logging.WARNING,
                    WARN = logging.WARNING,
                    INFO = logging.INFO,
                    DEBUG = logging.DEBUG,
                    NOTSET = logging.NOTSET))
        self.cfg.LOG_LEVEL = level
        self.cfg.logger.setLevel(getattr(level, configuration.get('log', 'level')))
        
    def _initPlugins(self, rootpath=''):
        if hasattr(self.cfg, 'plugins'):
            return self.cfg.plugins.loaded, self.cfg.plugins.failed
        self.cfg.plugins = Hook()
        self.cfg.plugins.all = {}
        self.cfg.plugins.loaded = set([])
        self.cfg.plugins.failed = set([])
        
        loaded, failed = loadPlugins(self, rootpath or self.cfg.path.rootdir, 'plugins')
        
        if failed :
            logger.error("\nFailed:=%s" % str(failed))
            
            rootPath = None
            
            if rootpath :
                rootPath = rootpath
            else :
                rootPath = self.cfg.path.rootdir
                
            logger.debug("\nRootPath:=%s" % str(rootPath))
        
        logger.debug("\nLoaded:=%s" % str(loaded))
        
        self.cfg.plugins.reload = partially(reloadPluginFeature, self)
        
        return loaded, failed
        
    def _initDirs(self):
        self.cfg.path = Hook()
        self.cfg.path.rootdir = SHELL_ROOT_DIR
        self.cfg.path.pluginsdir = os.path.join(self.cfg.path.rootdir, 'plugins')
        self.cfg.path.logdir = os.path.join(self.cfg.path.rootdir, 'log')
        
    def lookup(self, pattern):
        '''
        Locally looks up a regular expression pattern in agility-shell REST endpoints, service methods and plugins
        For example:
        agility.lookup('.*[v|V]olume')
        
        result: ['a.cloud.searchCloudVolumes',
                 'a.template.addVolume',
                 'a.template.deleteVolume',
                 'a.template.getVolumes',
                 'a.volume',
                 'a.volume.deleteVolume',
                 'a.volume.getVolume',
                 'a.volume.getVolumesXML',
                 'a.volumestorage',
                 'a.volumestorage.getVolumeStorage',
                 'a.volumestorage.getVolumeStoragesXML',
                 'a.volumestoragesnapshot',
                 'a.volumestoragesnapshot.getVolumeStorageSnapshot',
                 'a.volumestoragesnapshot.getVolumeStorageSnapshotSnapshotXML']
        
        @param pattern: regular expression
        @return: list of hook names
        '''
        import re
        matches = []
        for attrName in dir(self):
            if re.match(pattern, attrName):
                matches.append('a.%s'%attrName)
            attr = getattr(self, attrName)
            for attrName_ in dir(attr):
                if re.match(pattern, attrName_):
                    matches.append('a.%s.%s'%(attrName, attrName_))
        return matches
        
def init(configuration=None, conn=None, agility=None, logger=None):
    if not configuration:
        configuration = getConfiguration()

    config = configuration.getConfig(['main', 'apiversion'])
    client.setAPIVersion(config.apiversion_version)
    if not conn:
        conn = getConnection(config)
        if config.main_connect:
            conn.connect(host = config.main_host, username = config.main_username, password = config.main_password)
    if agility is None:
        print("Initializing agility...")
        agility = Agility(conn, configuration, logger=logger)
    else:
        agility.cfg.conn = conn
        agility._prefetch = config.main_prefetch
    
    agility.cfg.configuration = configuration
    universal.agility = universal.a = agility
    return agility


