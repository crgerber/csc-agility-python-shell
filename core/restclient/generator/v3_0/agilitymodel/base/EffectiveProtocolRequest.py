from AgilityModelBase import AgilityModelBase

class EffectiveProtocolRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, item=None, policyid=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'item': {'type': 'Link', 'name': 'item', 'minOccurs': '0', 'native': False}, 'policyId': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'policyid', 'minOccurs': '0', 'native': True}})
        self.item = item
        self.policyid = policyid 
