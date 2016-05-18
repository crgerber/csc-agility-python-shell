'''
Created on Oct 24, 2012

@author: dawood
'''

import csv
import os

from core.agility import getClient
from core.restclient import responseparser
import reporting
from core.agility.common.servicelookup import lookup

COMPONENT_NAME = reporting.LOGGER_NAME
import logger
logger = logger.getLogger(COMPONENT_NAME)
responseparser.register_parser(responseparser.PARSER.BEAUTIFUL_SOUP)
#responseparser.register_parser(responseparser.PARSER.LXML)
parse = responseparser.parser()

filters = {
           '1_simple_str_only' : lambda k, v=None: (None, None) if not isinstance(k if v is None else v, str) else (k, v),
           '2_to_str' : lambda k, v=None: (str(k), str(v)),
           '3_ignore_private' : lambda k, v=None: (None, None) if k.startswith('_') else (k, v)
           }

def applyFilters(sequence, **functions):
    #mixing filter and map actions iteratively
    isDict = isinstance(sequence, dict)
    put = lambda seq, item: seq.add(item) if isinstance(seq, set) else seq.append(item)
    result = {} if isDict else []
    for k in sequence:
        v = sequence[k] if isDict else None
        for funcName in sorted(functions):
            #apply the filter functions iteratively, returning None as key, skips the pair at hand
            k, v = functions[funcName](k, v)
            if not k: break
        else:
            result.update([(k, v)]) if isDict else put(result, k) #result.append(k)
    return result

def getAssetList(conn, assetName, getDetails=True, persist=True, persistRootDir='', persistFilePrefix=''):    
    serviceProxy = getattr(getClient(), assetName.lower())(conn)
    serviceName = lookup(assetName, lookup.ACTION.GET)
    service = getattr(serviceProxy, serviceName)
    summaryPersistDir = os.path.join(persistRootDir, conn.conn_params['host'], conn.conn_params['systemversion'], assetName, 'summary')
    persistFile = '%s%s%s.xml'%(persistFilePrefix, '_' if persistFilePrefix else '', assetName)
    assetList = parse(service(''), assetName, persistDir=summaryPersistDir if persist else '', persistFile=persistFile if persist else '')
    logger.info('Loaded [%s] %s summary entries', len(assetList), assetName)
    detailesPersistDir = os.path.join(persistRootDir, conn.conn_params['host'], conn.conn_params['systemversion'], assetName, 'details')
    detailedAssetList = [parse(service(c.id), assetName, persistDir=detailesPersistDir if persist else '', persistFile='%s_%s'%(c.id, persistFile) if persist else '') for c in assetList] if getDetails else []
    logger.info('Loaded [%s] %s detailed entries', len(detailedAssetList), assetName)
    return assetList, detailedAssetList

def _createAssetReport(envParams, assetList, detailedAssetList, assetName='', reportDir = '', reportFileName='', filters={}, cols=None):
    reportParams = dict(envParams)
    assetName = assetName or assetList[0].name
    reportParams['assetName'] = assetName
    reportParams['ext'] = 'csv'
    reportFileName = reportFileName or '%(host)s_%(systemversion)s_%(assetName)s_%(version)s.%(ext)s'%reportParams
    reportFilePath = os.path.join(reportDir, reportFileName)
    if not os.path.exists(reportDir):
        os.makedirs(reportDir)
    csv.register_dialect('excel', delimiter='|')
    
    with open(reportFilePath, 'w') as reportFile:
        logger.info('New report file %s created', reportFilePath)
        logger.info('Received [%s] %s entries', len(assetList), assetName)
        #filter out all the private attributes
        #filter out all the complex attributes, retaining only the string ones
        colNamesSet = set()
        [colNamesSet.add(key) for asset in detailedAssetList for key in list(asset._attrs.keys()) ]
        logger.info('Applying filters: %s', list(filters.keys()))
        cols = cols or applyFilters(colNamesSet, **filters)
        data = [applyFilters(asset._attrs, **filters) for asset in detailedAssetList]
        
        reportWriter = csv.DictWriter(reportFile, sorted(cols), dialect='excel', extrasaction='ignore')
        reportWriter.writeheader()
        reportWriter.writerows(data)
        logger.info('Report %s created successfully', reportFilePath)


def generateAssetReport(conn, assetName, reportDir = '', reportFileName='', filters={}):
    assetList, detailedAssetList = getAssetList(conn, assetName, getDetails=True)
    _createAssetReport(conn.conn_params, assetList, detailedAssetList, assetName, reportDir, reportFileName, filters)