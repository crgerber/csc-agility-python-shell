from core.agility.v3_0.agilitymodel.base.EffectiveProtocol import EffectiveProtocolBase
from core.agility.v3_0.agilitymodel.actions.EffectiveProtocol import EffectiveProtocolActions

class EffectiveProtocol(EffectiveProtocolBase, EffectiveProtocolActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, policyname=None, direction=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param policyname: policyname minOccurs=0
        @type policyname: string
        @param direction: direction minOccurs=0
        @type direction: string
        '''
        EffectiveProtocolBase.__init__(self, status=status, policyname=policyname, direction=direction)
