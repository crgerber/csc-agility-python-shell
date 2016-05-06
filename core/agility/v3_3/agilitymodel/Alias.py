from core.agility.v3_3.agilitymodel.base.Alias import AliasBase
from core.agility.v3_3.agilitymodel.actions.Alias import AliasActions

class Alias(AliasBase, AliasActions):
    '''
    classdocs
    '''
    def __init__(self, link=None):
        '''
        Constructor
        @param link: link minOccurs=0
        @type link: Link
        '''
        AliasBase.__init__(self, link=link)
