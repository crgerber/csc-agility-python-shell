from AgilityModelBase import AgilityModelBase

class CloudMetaModelBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, onboardMeta=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'onboardMeta': {'maxOccurs': 'unbounded', 'type': 'OnboardMeta', 'name': 'onboardMeta', 'minOccurs': '0', 'native': False}})
        self.onboardMeta = onboardMeta 
