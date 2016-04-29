from core.agility.common.AgilityModelBase import AgilityModelBase

class CloudMetaModelBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, onboardmeta=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'onboardMeta': {'maxOccurs': 'unbounded', 'native': False, 'name': 'onboardmeta', 'minOccurs': '0', 'type': 'OnboardMeta'}})
        self.onboardmeta = onboardmeta 
