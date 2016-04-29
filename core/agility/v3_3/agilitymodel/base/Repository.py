from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class RepositoryBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, path=None, size=None, repositorytype=None, properties=[], cloud=None, usage=[], locations=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'native': True, 'name': 'path', 'minOccurs': '0', 'type': 'string'}, 'size': {'native': True, 'name': 'size', 'minOccurs': '0', 'type': 'long'}, 'repositoryType': {'native': True, 'name': 'repositorytype', 'minOccurs': '0', 'type': 'string'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'locations': {'maxOccurs': 'unbounded', 'native': True, 'name': 'locations', 'minOccurs': '0', 'type': 'string'}, 'usage': {'maxOccurs': 'unbounded', 'native': False, 'name': 'usage', 'minOccurs': '0', 'type': 'RepositoryUsage'}})
        self.path = path
        self.size = size
        self.repositorytype = repositorytype
        self.properties = properties
        self.cloud = cloud
        self.usage = usage
        self.locations = locations 
