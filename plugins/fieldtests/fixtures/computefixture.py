'''
Created on Oct 24, 2012

@author: dawood
'''

from fixtures.basefixture import BaseFixture
import fixtures
import logger
COMPONENT_NAME = 'agility-testbench'
logger = logger.getLogger('%s.%s'%(COMPONENT_NAME, __name__))



class ComputeFixture(BaseFixture):
    '''
    includes setup and tear down for script creation, plus helper methods
    '''
    
    def __init__(self, conn=None, assetName='Compute', snapshot=BaseFixture.SNAPSHOT.NEW, **kwargs):
        BaseFixture.__init__(self, conn, assetName, snapshot, **kwargs)
        
    def _selectReportFilters(self, filters):
        selectedFilters = dict(filters)
        return selectedFilters
        
    def _serviceNameOrPattern(self):
        return 'getInstance' 
        
        