from core.agility.v2_0.agilitymodel.base.Policy import PolicyBase
from core.agility.v2_0.agilitymodel.actions.Policy import PolicyActions

class Policy(PolicyBase, PolicyActions):
    '''
    classdocs
    '''
    def __init__(self, filter=None, definition=None, type=None, apiVersion=None):
        '''
        Constructor
        @param filter: filter minOccurs=0
        @type filter: string
        @param definition: definition minOccurs=0
        @type definition: string
        @param type: type minOccurs=0
        @type type: PolicyType
        @param apiVersion: apiVersion minOccurs=0
        @type apiVersion: string
        '''
        PolicyBase.__init__(self, filter=filter, definition=definition, type=type, apiVersion=apiVersion)
