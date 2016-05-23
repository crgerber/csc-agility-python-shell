from core.agility.common.AgilityModelBase import AgilityModelBase

class EffectiveProtocolRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, policyid=[], item=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'policyId': {'name': 'policyid', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'int'}, 'item': {'name': 'item', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.policyid = policyid
        self.item = item 
