from core.restclient.v2_0.agilitymodel.base.AliasList import AliasListBase
from core.restclient.v2_0.agilitymodel.actions.AliasList import AliasListActions

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
