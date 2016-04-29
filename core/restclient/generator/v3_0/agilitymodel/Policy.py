from .base.Policy import PolicyBase
from .actions.Policy import PolicyActions

class Policy(PolicyBase, PolicyActions):
    '''
    classdocs
    '''
    def __init__(self, filter=None, definition=None, type=None, apiversion=None):
        '''
        Constructor
        @param filter: filter minOccurs=0
        @type filter: string
        @param definition: definition minOccurs=0
        @type definition: string
        @param type: type minOccurs=0
        @type type: PolicyType
        @param apiversion: apiversion minOccurs=0
        @type apiversion: string
        '''
        PolicyBase.__init__(self, filter=filter, definition=definition, type=type, apiversion=apiversion)
