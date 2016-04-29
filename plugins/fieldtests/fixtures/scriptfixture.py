'''
Created on Oct 18, 2012

@author: dawood
'''
from fixtures.basefixture import BaseFixture
import fixtures
from core.restclient import responseparser
from gen import methods as client
from core.restclient.responseparser.ParserLxml import xml2d
from . import xmltemplates
import logger
COMPONENT_NAME = 'agility-testbench'
logger = logger.getLogger('%s.%s'%(COMPONENT_NAME, __name__))


parse = responseparser.parser()

class ScriptFixture(BaseFixture):
    '''
    includes setup and tear down for script creation, plus helper methods
    '''

    def __init__(self, conn=None, assetName='Script', snapshot=BaseFixture.SNAPSHOT.NEW):
        BaseFixture.__init__(self, conn, assetName, snapshot)
        self.newScript = None
        self.scriptService = client.script(self.conn)
        self.templateScript = None
        
    def setUp(self):
        BaseFixture.setUp(self)
        self.templateScript = lambda : responseparser.createProxy(xml2d(xmltemplates.SCRIPT), 'Script')
        
    def tearDown(self):
        if self.newScript:
            self.scriptService.deleteScript(self.newScript.id)
        BaseFixture.tearDown(self)
        
    def _selectReportFilters(self, filters):
        selectedFilters = dict(filters)
#         disabledFilter = selectedFilters.pop('1_simple_str_only')
        selectedFilters['100_remove_script_body_col'] = lambda k, v: (None, None) if k== 'body' else (k, v)
        return selectedFilters
        
    def createScript(self, parentAsset, parentAssetId, scriptName, scriptDesc, scriptBody='', *deleteVars, **extendedVars):
        '''
        @param parentAsset: default 'project' OR 'environment'
        '''
        deleteVars = deleteVars# or ['Script_id', 'Script_uuid', 'Script_created', 'Script_lastModified', 'Script_body', 'Script_slot', 'Script_version', 'Script_slotId']
        extendedVars.update(dict(Script_name=scriptName, Script_description=scriptDesc, Script_body=scriptBody))
        template, templateVars = self.templateScript().createTemplate(*deleteVars, **extendedVars)
        parentService = getattr(client, parentAsset)(self.conn)
        self.newScript = parse(parentService.createScript(parentAssetId, template%templateVars))
        return self.newScript
    
        
        
        
        