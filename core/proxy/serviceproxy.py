'''
Created on Oct 22, 2012

@author: dawood
'''
import os
from functools import update_wrapper

from core.agility import getClient
from core.restclient import responseparser
from core.restclient.responseparser.common import AbstractProxy
from core.agility.common.servicelookup import lookup

responseparser.register_parser(responseparser.PARSER.LXML_MODEL)
parse = responseparser.parser()

import logger
logger = logger.getLogger(__name__)
        
class ParseDecorator(object):
    _parse = parse
    def __init__(self, assetName):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.assetName = assetName

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        def wrapped_f(*args, **kwargs):
            result = f(*args, **kwargs)
        
            if isinstance(result, bytes):
                return ParseDecorator._parse(str(result, encoding='utf-8'), self.assetName)
            elif isinstance(result, str):
                return ParseDecorator._parse(result, self.assetName)
            else:
                result.assetType = self.assetName
                return result
            
        return update_wrapper(wrapped_f, f)

class FilterDecorator(object):
    '''
    Instance method decorator
    '''
    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        self.f = f
        update_wrapper(self, f)
        
    def __get__(self, instance, cls=None):
        self._instance = instance
        return self
    
    def __call__(self, *args, **kwargs):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        prefix = 'filter_'
        filters = [argitem for argitem in list(kwargs.items()) if argitem[0].startswith(prefix)]
        [kwargs.pop(f[0]) for f in filters]
        filters = [(k[len(prefix):], v) for k, v in filters]
        result = self.f(self._instance, *args, **kwargs)
        
        if not filters:
            logger.debug('No active filters') 
            return result
        logger.debug('Applying filters [%s]'%filters)
        filteredResult = []
        if not isinstance(result, (tuple, list)): result = [result]

        for item in result:
            boolResults = [getattr(item, f[0]) == f[1] for f in filters]
            if all(boolResults):
                filteredResult.append(item)

        return filteredResult
        

class ServiceProxy(AbstractProxy):
    '''
    Service end-point proxy object, configurable to pre-fetch object hierarchy or perform manual loading
    '''
    def __init__(self, conn, assetName='', prefetch=True, autoParse=True):
        AbstractProxy.__init__(self, typeName=assetName)
        self._autoattrs += ['_conn', '_prefetch', '_client', '_service', '_autoParse']
        self._conn = conn
        self._prefetch = prefetch
        self._autoParse = autoParse
        self._client = getClient()
        service = getattr(self._client, assetName.lower(), None)
        if service:
            self._service = service(conn)
        else:
            raise RuntimeError('Invalid service endpoint: %s'%assetName.lower())
            
    def __dir__(self):
        serviceAttrs = dir(self._service)
        return AbstractProxy.__dir__(self) + serviceAttrs
    
    def __iter__(self):
        '''
        __iter__ is modified to return only the available service endpoints
        '''
        endpoints = [attr for attr in dir(self._service) if not attr.startswith('_')]
        return iter(endpoints)
    
    def _newSubObject(self, attrs):
        raise NotImplementedError('Sub object factory method is not defined for type: %s self.__class__.__name__')
    
    def __getattr__(self, name):
        result = None
        if name in object.__getattribute__(self, '_autoattrs'):
            result = object.__getattribute__(self, name)
        elif name in object.__getattribute__(self, '_attrs'):
            result = self.__getitem__(name)
        else:
            method = getattr(self._service, name, None)
            if not method:
                raise AttributeError(name)
            result = ParseDecorator(self.typeName)(method) if self._autoParse else method
            result.context = method.context
        return result

    @FilterDecorator
    def listSummary(self, persist=False, persistRootDir='snapshot', persistFilePrefix='agilityshell_'):
        assetList, detailedAssetList = self.getAssetLists(persist, persistRootDir, persistFilePrefix, getDetails=False)
        return assetList
    
    @FilterDecorator
    def listDetails(self, persist=False, persistRootDir='snapshot', persistFilePrefix='agilityshell_'):
        assetList, detailedAssetList =  self.getAssetLists(persist, persistRootDir, persistFilePrefix, getDetails=True)
        return detailedAssetList
        
    def getAssetLists(self, persist=False, persistRootDir='snapshot', persistFilePrefix='agilityshell_', getDetails=True):
        assetList, detailedAssetList = self._getAssetLists(self._conn, self.typeName, getDetails=getDetails, persist=persist, persistRootDir=persistRootDir, persistFilePrefix=persistFilePrefix)
        return assetList, detailedAssetList
    
    def _getAssetLists(self, conn, assetName, getDetails=True, persist=True, persistRootDir='', persistFilePrefix=''):
        '''
        almost duplicates getAssetList from the reporter module, copied here to break the dependency
        '''    
        serviceProxy = getattr(self._client, assetName.lower())(conn)
        serviceName = lookup(assetName.lower(), action=lookup.ACTION.GET)
        service = getattr(serviceProxy, serviceName)
        summaryPersistDir = os.path.join(persistRootDir, conn.conn_params['host'], conn.conn_params['systemversion'], assetName, 'summary')
        persistFile = '%s%s%s.xml'%(persistFilePrefix, '_' if persistFilePrefix else '', assetName)
        assetList = parse(service(''), assetName, persistDir=summaryPersistDir if persist else '', persistFile=persistFile if persist else '')
        logger.info('Loaded [%s] %s summary entries', len(assetList), assetName)
        detailesPersistDir = os.path.join(persistRootDir, conn.conn_params['host'], conn.conn_params['systemversion'], assetName, 'details')
        detailedAssetList = [parse(service(c.id), assetName, persistDir=detailesPersistDir if persist else '', persistFile='%s_%s'%(c.id, persistFile) if persist else '') for c in assetList] if getDetails else []
        logger.info('Loaded [%s] %s detailed entries', len(detailedAssetList), assetName)
        return assetList, detailedAssetList
    
