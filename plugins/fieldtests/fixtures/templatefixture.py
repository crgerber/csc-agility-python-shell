'''
Created on Oct 24, 2012

@author: dawood
'''

from fixtures.basefixture import BaseFixture
import fixtures
import logger
COMPONENT_NAME = 'agility-testbench'
logger = logger.getLogger('%s.%s'%(COMPONENT_NAME, __name__))



class TemplateFixture(BaseFixture):
    '''
    includes setup and tear down for script creation, plus helper methods
    '''
    
    def __init__(self, conn=None, assetName='Template', snapshot=BaseFixture.SNAPSHOT.NEW):
        BaseFixture.__init__(self, conn, assetName, snapshot)
        
    def _selectReportFilters(self, filters):
        selectedFilters = dict(filters)
        disabledFilter = selectedFilters.pop('1_simple_str_only')
        return selectedFilters
        
        
        