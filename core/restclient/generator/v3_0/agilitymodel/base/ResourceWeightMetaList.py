from .AgilityModelBase import AgilityModelBase

class ResourceWeightMetaListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resourceweightmeta=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceWeightMeta': {'maxOccurs': 'unbounded', 'type': 'ResourceWeightMeta', 'name': 'resourceweightmeta', 'minOccurs': '0', 'native': False}})
        self.resourceweightmeta = resourceweightmeta 
