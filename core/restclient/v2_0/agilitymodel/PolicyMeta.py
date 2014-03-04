from core.restclient.v2_0.agilitymodel.base.PolicyMeta import PolicyMetaBase
from core.restclient.v2_0.agilitymodel.actions.PolicyMeta import PolicyMetaActions

class PolicyMeta(PolicyMetaBase, PolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, type=''):
        '''
        Constructor
        @param type: type
        @type type: string
        '''
        PolicyMetaBase.__init__(self, type=type)
