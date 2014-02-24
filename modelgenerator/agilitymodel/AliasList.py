from base.AliasList import AliasListBase
from actions.AliasList import AliasListActions

class AliasList(AliasListBase, AliasListActions):
    '''
    classdocs
    '''
    def __init__(self, alias=list()):
        '''
        Constructor
        @param alias: alias minOccurs=0 maxOccurs=unbounded
        @type alias: Alias
        '''
        AliasListBase.__init__(self, alias=alias)
