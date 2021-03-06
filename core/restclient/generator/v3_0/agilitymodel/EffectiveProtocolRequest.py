from base.EffectiveProtocolRequest import EffectiveProtocolRequestBase
from actions.EffectiveProtocolRequest import EffectiveProtocolRequestActions

class EffectiveProtocolRequest(EffectiveProtocolRequestBase, EffectiveProtocolRequestActions):
    '''
    classdocs
    '''
    def __init__(self, item=None, policyid=[]):
        '''
        Constructor
        @param item: item minOccurs=0
        @type item: Link
        @param policyid: policyid minOccurs=0 maxOccurs=unbounded
        @type policyid: int
        '''
        EffectiveProtocolRequestBase.__init__(self, item=item, policyid=policyid)
