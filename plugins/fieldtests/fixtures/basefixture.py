'''
Created on Oct 24, 2012

@author: dawood
'''
import os
from unittest import TestCase
import fixtures
from core.restclient import client
import logger
COMPONENT_NAME = 'agility-testbench'
logger = logger.getLogger('%s.%s'%(COMPONENT_NAME, __name__))

from agilityshell import agility
agility._initPlugins()
loadSnapshot = agility.tools.snapshot.loadSnapshot
loadSnapshots = agility.tools.snapshot.loadSnapshots
getAssetList = agility.tools.report.getAssetList
createAssetReport = agility.tools.report._createAssetReport

filters = {
           '1_simple_str_only' : lambda k, v=None: (None, None) if not isinstance(k if v is None else v, str) else (k, v),
           '2_to_str' : lambda k, v=None: (str(k), str(v)),
           '3_ignore_private' : lambda k, v=None: (None, None) if k.startswith('_') else (k, v)
           }
class _SNAPSHOT():
    NEW = 'snapshot'
    LOAD = 'load'
    
class BaseFixture(TestCase):
    '''
    base class for AssetFixture(s), includes asset enumerations, xml snapshot, xml load and compare capabilities
    '''
    SNAPSHOT = _SNAPSHOT()
    
    def __init__(self, conn, assetName='', snapshot=_SNAPSHOT.NEW):
        self.conn = conn
        self.assetName = assetName
        self.snapshot = snapshot
        self.configured = False
    
    def configure(self, client='', baseDir='', createCSVReport=True, 
                  recreateCSVReport=False, detailedReport=True):
        
        logger.info('%s.configure'%self.__class__.__name__)
        self.client = client
        self.environment = self.conn.conn_params['host']
        self.systemversion = self.conn.conn_params['systemversion']
        self.apiversion = self.conn.conn_params['version']
        self.baseDir = baseDir
        self.persistDir = os.path.join(self.baseDir, 'environments')
        self.reportDir = os.path.join(self.baseDir, 'reports')
        self.createCSVReport = createCSVReport
        self.recreateCSVReport = recreateCSVReport#recreate the report from loaded XML xnapshot
        self.detailedReport = detailedReport
        self.compareAttrs = None
        self.configured = True
        return self
    
    def _selectReportFilters(self, filters):
        selectedFilters = dict(filters)
        disabledFilter = selectedFilters.pop('1_simple_str_only')
        return selectedFilters
    
    def _selectCompareAttrs(self, detailedAssetList):
        return None#None => include all attrs in reports
    
    def setUp(self):
        '''
        if setUp is overridden by subclasses, the base fixture setup should be called from within the method body
        '''
        if not self.configured:
            raise RuntimeError('Fixture is not configured properly')
        logContext = {'host' : self.conn.conn_params['host'],
                      'systemversion' : self.conn.conn_params['systemversion'],
                      'apiversion' : self.conn.conn_params['version'],
                      'assetName' : self.assetName}
        logger.info('%s.setUp'%self.__class__.__name__)
        assetList = []
        detailedAssetList = []
        host = self.conn.conn_params['host']
        if self.snapshot == self.SNAPSHOT.NEW:
            logger.info('Creating a new snapshot: %(host)s.%(systemversion)s.%(apiversion)s.%(assetName)s'%logContext)
            assetList, detailedAssetList = getAssetList(self.conn, self.assetName, getDetails=self.detailedReport, persistRootDir=self.persistDir)
            if self.createCSVReport:
                cols = self._selectCompareAttrs(detailedAssetList)
                createAssetReport(assetList, detailedAssetList, assetName=self.assetName, reportDir=self.reportDir, filters=self._selectReportFilters(filters), cols=cols)
        elif self.snapshot == self.SNAPSHOT.LOAD:
            snapshot = loadSnapshots(self.persistDir, self.assetName, host, systemversion=self.systemversion)
            assetList = snapshot[host][self.systemversion][self.assetName][loadSnapshot.SUMMARY]
            detailedAssetList = snapshot[host][self.systemversion][self.assetName][loadSnapshot.DETAILS]
                    
            if self.recreateCSVReport:
                cols = self._selectCompareAttrs(detailedAssetList)
                createAssetReport(assetList, detailedAssetList, assetName=self.assetName, reportDir=self.reportDir, filters=self._selectReportFilters(filters), cols=cols)

        self.assetList = assetList
        self.detailedAssetList = detailedAssetList
        

    
    def tearDown(self):
        logger.info('tearDown')
        
        
        
        