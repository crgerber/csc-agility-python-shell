from core.restclient.v2_0.agilitymodel.base.EffectiveProtocol import EffectiveProtocolBase
from core.restclient.v2_0.agilitymodel.actions.EffectiveProtocol import EffectiveProtocolActions

class EffectiveProtocol(EffectiveProtocolBase, EffectiveProtocolActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, policyName=None, direction=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param policyName: policyName minOccurs=0
        @type policyName: string
        @param direction: direction minOccurs=0
        @type direction: string
        '''
        EffectiveProtocolBase.__init__(self, status=status, policyName=policyName, direction=direction)
