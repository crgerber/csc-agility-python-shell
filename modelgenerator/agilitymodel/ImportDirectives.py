from base.ImportDirectives import ImportDirectivesBase
from actions.ImportDirectives import ImportDirectivesActions

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
