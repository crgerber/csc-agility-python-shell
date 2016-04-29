from core.agility.common.AgilityModelBase import AgilityModelBase

class EffectiveProtocolRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, policyid=[], item=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'policyId': {'maxOccurs': 'unbounded', 'native': True, 'name': 'policyid', 'minOccurs': '0', 'type': 'int'}, 'item': {'native': False, 'name': 'item', 'minOccurs': '0', 'type': 'Link'}})
        self.policyid = policyid
        self.item = item 
