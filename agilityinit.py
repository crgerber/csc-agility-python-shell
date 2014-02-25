'''
Created on Nov 16, 2012

@author: dawood
'''
####################### <BEGIN> KEEP THE FOLLOWING INIT CODE ON TOP OF EVERYTHING ELSE ###########################
import os, sys
#the following trick can't be done from the agilityshell.py file, since the main entry point with __name__ == '__main__' might not have a __file__ attribute, depending on the Python implementation for the underlying platform
SHELL_ROOT_DIR = os.path.dirname(sys.modules[__name__].__file__)
import logging
import logger
logger.configRootLogger('agilityshell', os.path.join(SHELL_ROOT_DIR, 'logs'), 'agilityshell.log', logging.DEBUG, console=True) 
####################### <END> KEEP THE FOLLOWING INIT CODE ON TOP OF EVERYTHING ELSE ###########################
from logger import logger
from core.pyworx import pythonpath
from core.pyworx.partialfunc import partially
from core.config.configuration import AgilityShellConfig

srcfolders = ['.', SHELL_ROOT_DIR, 'lib/beautifulsoup4-4.1.3', 'lib/ipython-0.13.1']
pythonpath.addPaths(srcfolders, basedir=SHELL_ROOT_DIR)
from core.base.enum import Enum
from core.proxy.serviceproxy import ServiceProxy
from core.proxy.hook import Hook

from core.plugin import loadPlugins, reloadPluginFeature
from shellutils.utils import Tools
from core.restclient.connection import RESTConnection
from core.restclient.search.query import AgilityQuery
from core import universal

import inspect
def getConfiguration(path=None):
    path = path or os.path.join(SHELL_ROOT_DIR, 'agilityshell.cfg')
    configuration = AgilityShellConfig(path=path)
    return configuration

def configure(config=None):
    config = config or getConfiguration()
    return config

def getConnection(config):
    conn = RESTConnection(auth=config.main_auth, host=config.main_host, username=config.main_username, password=config.main_password,
                          stemversion=config.main_systemversion, version=config.apiversion_version, use_cookies=config.main_use_cookies,
                          reauthenticate=config.main_reauthenticate)
    return conn


def query(**kwargs):
    return AgilityQuery(**kwargs)

class Agility(object):
    def __init__(self, conn, configuration, assetName='ROOT'):
        self.cfg = Hook()
        self.cfg.conn = conn
        prefetch = configuration.get('main', 'prefetch')
        self._services = ['address',
 'addressrange',
 'alias',
 'artifact',
 'artifactattachment',
 'artifacttype',
 'assettype',
 'attachment',
 'auth',
 'authtype',
 'blueprint',
 'blueprint_designcontainer',
 'blueprint_workload',
 'cloud',
 'cloudtype',
 'compute',
 'configuration_artifact',
 'configuration_artifacttype',
 'configuration_policy',
 'configuration_repository',
 'configuration_resource',
 'connection',
 'container',
 'credential',
 'custom',
 'customcontainer',
 'deployer',
 'designdeployer',
 'dhcpoptions',
 'domain',
 'environment',
 'environmenttype',
 'resources',
 'eula',
 'globals',
 'image',
 'launchitem',
 'launchitemdeployment',
 'ldapgroup',
 'location',
 'model',
 'network',
 'networkinterface',
 'networkservice',
 'networkservicetype',
 'onboard',
 'os',
 'paas',
 'paastype',
 'package',
 'permissiontype',
 'policy',
 'project',
 'projectrole',
 'propertygroup',
 'propertytype',
 'reports',
 'repository',
 'runtime',
 'script',
 'scriptclasspath',
 'scriptlanguage',
 'search',
 'security',
 'servicebindingtype',
 'setup',
 'solution',
 'solutiondeployment',
 'stack',
 'storage',
 'storecatalog',
 'storecategory',
 'storeedition',
 'storeproduct',
 'storeproductadapter',
 'storeproducttype',
 'storerelease',
 'targetcloud',
 'task',
 'template',
 'theme',
 'topology',
 'tree',
 'user',
 'usergroup',
 'variable',
 'volume',
 'volumestorage',
 'volumestoragesnapshot']
        self._assetNames = [assetName.title() for assetName in self._services]
        [object.__setattr__(self, serviceName, ServiceProxy(conn, serviceName.title(), prefetch)) for serviceName in self._services]
        self._initLogger(configuration)
        self._initDirs()
        self.tools = Tools()
        
    
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
    
    def _initLogger(self, configuration):
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
        
def init(configuration=None, conn=None, agility=None):
    if not configuration:
        configuration = getConfiguration()
        config = configuration.getConfig(['main', 'apiversion'])
    if not conn:
        conn = getConnection(config)
        if config.main_connect:
            conn.connect()
    if agility is None:
        agility = Agility(conn, configuration)
    else:
        agility.cfg.conn = conn
        agility._prefetch = config.main_prefetch
    
    agility.cfg.configuration = configuration
    universal.agility = universal.a = agility
    return agility


