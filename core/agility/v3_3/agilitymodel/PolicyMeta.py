from core.agility.v3_3.agilitymodel.base.PolicyMeta import PolicyMetaBase
from core.agility.v3_3.agilitymodel.actions.PolicyMeta import PolicyMetaActions

class PolicyMeta(PolicyMetaBase, PolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, type='', availablescopes=[]):
        '''
        Constructor
        @param type: type
        @type type: string
        @param availablescopes: availablescopes minOccurs=0 maxOccurs=unbounded
        @type availablescopes: string
        '''
        PolicyMetaBase.__init__(self, type=type, availablescopes=availablescopes)
