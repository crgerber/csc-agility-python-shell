from AgilityModelBase import AgilityModelBase

class ResourceWeightMetaListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resourceWeightMeta=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceWeightMeta': {'maxOccurs': 'unbounded', 'type': 'ResourceWeightMeta', 'name': 'resourceWeightMeta', 'minOccurs': '0', 'native': False}})
        self.resourceWeightMeta = resourceWeightMeta 
