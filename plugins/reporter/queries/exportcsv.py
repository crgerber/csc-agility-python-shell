'''
Created on Oct 29, 2012

@author: dawood
'''
from agilityshell import agility
import reporting
from reporting.csvwriter import writeCSVFile
from core.restclient.agility.servicelookup import lookup
COMPONENT_NAME = reporting.LOGGER_NAME
import logger
logger = logger.getLogger(COMPONENT_NAME)

selectFields = agility.tools.scripting.selectFields

def customReport(data, reportFileName, reportDir='reports', fields=None, ignore=False, default='', delimiter='|', ext=''):
    '''
    @param data: sequence of [maps or objects]
    '''
    data = [selectFields(item, fields, ignore=ignore, default=default) for item in data]
    writeCSVFile(data, '%s%s%s'%(reportFileName, '.' if ext else '', ext), reportDir, fields, delimiter=delimiter)

def exportSearchResultsCSV(agility, assetName, query, reportDir='reports', reportFileName=''):
    '''
    exports search results, obtained by calling the asset's search API 
    with the specified query to a CSV file with name <reportFileName> under directory <rerpotDir>
    
    Plugin: a.tools.report, Adhering to the serviceMethod signature func(agility, assetName, *args, **kwargs)
    
    @param query: populated AgilityQuery instance
    @param reportDir: target directory for the report, default: reports
    @param reportFileName: report file name, default: '%(host)s_%(assetName)s_%(version)s.%(ext).csv
    '''
    serviceProxy = getattr(agility, assetName.lower())
    searchService = getattr(serviceProxy, lookup(assetName, lookup.ACTION.SEARCH))
    result = searchService(**query.compile())
    logger.info('Received [%s] %s entries', len(result), assetName)
    ######################################################
    reportParams = dict(agility.cfg.conn.conn_params)
    reportParams['assetName'] = assetName
    reportParams['ext'] = 'csv'
    reportFileName = reportFileName or '%(host)s_%(assetName)s_%(version)s.%(ext)s'%reportParams
    colNamesSet = set()
    [colNamesSet.add(key) for asset in result for key in asset._attrs.keys()]
    cols = query.params.fields or colNamesSet
    data = [asset._attrs for asset in result]
    writeCSVFile(data, reportFileName, reportDir, cols)

def exportCSV(agility, assetName, reportDir='reports'):
    '''
    Exports all asset entries to a CSV report with default name: %(host)s_%(systemversion)s_%(assetName)s_%(version)s.CSV
    under the rerpotDir
    
    Plugin: a.tools.report, Adhering to the serviceMethod signature func(agility, assetName, *args, **kwargs)
    
    @param reportDir: target report directory, default: reports
    '''
    serviceProxy = getattr(agility, assetName.lower())
    assetList, detailedAssetList = serviceProxy.getAssetLists()
    reporter._createAssetReport(agility.cfg.conn.conn_params, assetList, detailedAssetList, 
                               assetName=assetName, reportDir=reportDir, filters=reporter.filters)