from core.agility.v3_3.agilitymodel.base.Policy import PolicyBase
from core.agility.v3_3.agilitymodel.actions.Policy import PolicyActions

class Policy(PolicyBase, PolicyActions):
    '''
    classdocs
    '''
    def __init__(self, filter=None, scope=None, apiversion=None, type=None, definition=None):
        '''
        Constructor
        @param filter: filter minOccurs=0
        @type filter: string
        @param scope: scope minOccurs=0
        @type scope: string
        @param apiversion: apiversion minOccurs=0
        @type apiversion: string
        @param type: type minOccurs=0
        @type type: PolicyType
        @param definition: definition minOccurs=0
        @type definition: string
        '''
        PolicyBase.__init__(self, filter=filter, scope=scope, apiversion=apiversion, type=type, definition=definition)
