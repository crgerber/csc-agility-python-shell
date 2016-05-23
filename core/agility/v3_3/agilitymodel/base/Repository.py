from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class RepositoryBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, size=None, cloud=None, properties=[], repositorytype=None, path=None, usage=[], locations=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'name': 'path', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'repositoryType': {'name': 'repositorytype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'size': {'name': 'size', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'usage': {'name': 'usage', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'RepositoryUsage'}, 'locations': {'name': 'locations', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.size = size
        self.cloud = cloud
        self.properties = properties
        self.repositorytype = repositorytype
        self.path = path
        self.usage = usage
        self.locations = locations 
