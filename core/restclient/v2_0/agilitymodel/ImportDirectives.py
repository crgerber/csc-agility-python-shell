from core.restclient.v2_0.agilitymodel.base.ImportDirectives import ImportDirectivesBase
from core.restclient.v2_0.agilitymodel.actions.ImportDirectives import ImportDirectivesActions

class ImportDirectives(ImportDirectivesBase, ImportDirectivesActions):
    '''
    classdocs
    '''
    def __init__(self, onNotFound=None):
        '''
        Constructor
        @param onNotFound: onNotFound
        @type onNotFound: LookupFailCode
        '''
        ImportDirectivesBase.__init__(self, onNotFound=onNotFound)
