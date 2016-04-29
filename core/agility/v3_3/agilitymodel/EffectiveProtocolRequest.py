from core.agility.v3_3.agilitymodel.base.EffectiveProtocolRequest import EffectiveProtocolRequestBase
from core.agility.v3_3.agilitymodel.actions.EffectiveProtocolRequest import EffectiveProtocolRequestActions

class EffectiveProtocolRequest(EffectiveProtocolRequestBase, EffectiveProtocolRequestActions):
    '''
    classdocs
    '''
    def __init__(self, policyid=[], item=None):
        '''
        Constructor
        @param policyid: policyid minOccurs=0 maxOccurs=unbounded
        @type policyid: int
        @param item: item minOccurs=0
        @type item: Link
        '''
        EffectiveProtocolRequestBase.__init__(self, policyid=policyid, item=item)
