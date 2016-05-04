from core.agility.common.AgilityModelBase import AgilityModelBase

class PolicyMetaModelBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, policymeta=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'policyMeta': {'maxOccurs': 'unbounded', 'type': 'PolicyMeta', 'name': 'policymeta', 'minOccurs': '0', 'native': False}})
        self.policymeta = policymeta 
