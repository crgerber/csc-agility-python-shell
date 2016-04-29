from .base.ImportDirectives import ImportDirectivesBase
from .actions.ImportDirectives import ImportDirectivesActions

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
