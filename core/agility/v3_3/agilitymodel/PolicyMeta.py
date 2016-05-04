from base.PolicyMeta import PolicyMetaBase
from actions.PolicyMeta import PolicyMetaActions

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
