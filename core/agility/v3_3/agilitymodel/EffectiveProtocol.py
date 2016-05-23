from core.agility.v3_3.agilitymodel.base.EffectiveProtocol import EffectiveProtocolBase
from core.agility.v3_3.agilitymodel.actions.EffectiveProtocol import EffectiveProtocolActions

class EffectiveProtocol(EffectiveProtocolBase, EffectiveProtocolActions):
    '''
    classdocs
    '''
    def __init__(self, policyname=None, direction=None, status=None):
        '''
        Constructor
        @param policyname: policyname minOccurs=0
        @type policyname: string
        @param direction: direction minOccurs=0
        @type direction: string
        @param status: status minOccurs=0
        @type status: string
        '''
        EffectiveProtocolBase.__init__(self, policyname=policyname, direction=direction, status=status)
