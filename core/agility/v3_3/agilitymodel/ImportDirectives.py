from core.agility.v3_3.agilitymodel.base.ImportDirectives import ImportDirectivesBase
from core.agility.v3_3.agilitymodel.actions.ImportDirectives import ImportDirectivesActions

class ImportDirectives(ImportDirectivesBase, ImportDirectivesActions):
    '''
    classdocs
    '''
    def __init__(self, onnotfound=None):
        '''
        Constructor
        @param onnotfound: onnotfound
        @type onnotfound: LookupFailCode
        '''
        ImportDirectivesBase.__init__(self, onnotfound=onnotfound)
