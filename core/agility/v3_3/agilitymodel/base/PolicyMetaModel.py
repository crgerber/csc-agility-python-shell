from core.agility.common.AgilityModelBase import AgilityModelBase

class PolicyMetaModelBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, policymeta=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'policyMeta': {'name': 'policymeta', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PolicyMeta'}})
        self.policymeta = policymeta 
