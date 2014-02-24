from AgilityModelBase import AgilityModelBase

class EffectiveProtocolRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, item=None, policyId=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'item': {'type': 'Link', 'name': 'item', 'minOccurs': '0', 'native': False}, 'policyId': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'policyId', 'minOccurs': '0', 'native': True}})
        self.item = item
        self.policyId = policyId 
