from base.Policy import PolicyBase
from actions.Policy import PolicyActions

class Policy(PolicyBase, PolicyActions):
    '''
    classdocs
    '''
    def __init__(self, filter=None, scope=None, type=None, apiversion=None, definition=None):
        '''
        Constructor
        @param filter: filter minOccurs=0
        @type filter: string
        @param scope: scope minOccurs=0
        @type scope: string
        @param type: type minOccurs=0
        @type type: PolicyType
        @param apiversion: apiversion minOccurs=0
        @type apiversion: string
        @param definition: definition minOccurs=0
        @type definition: string
        '''
        PolicyBase.__init__(self, filter=filter, scope=scope, type=type, apiversion=apiversion, definition=definition)
