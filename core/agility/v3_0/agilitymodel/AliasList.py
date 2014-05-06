from core.agility.v3_0.agilitymodel.base.AliasList import AliasListBase
from core.agility.v3_0.agilitymodel.actions.AliasList import AliasListActions

class AliasList(AliasListBase, AliasListActions):
    '''
    classdocs
    '''
    def __init__(self, alias=[]):
        '''
        Constructor
        @param alias: alias minOccurs=0 maxOccurs=unbounded
        @type alias: Alias
        '''
        AliasListBase.__init__(self, alias=alias)
