from AgilityModelBase import AgilityModelBase

class PolicyMetaModelBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, policyMeta=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'policyMeta': {'maxOccurs': 'unbounded', 'type': 'PolicyMeta', 'name': 'policyMeta', 'minOccurs': '0', 'native': False}})
        self.policyMeta = policyMeta 
