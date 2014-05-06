from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class RepositoryBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, repositorytype=None, locations=[], usage=[], path=None, properties=[], cloud=None, size=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'repositoryType': {'type': 'string', 'name': 'repositorytype', 'minOccurs': '0', 'native': True}, 'locations': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'locations', 'minOccurs': '0', 'native': True}, 'usage': {'maxOccurs': 'unbounded', 'type': 'RepositoryUsage', 'name': 'usage', 'minOccurs': '0', 'native': False}, 'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'size': {'type': 'long', 'name': 'size', 'minOccurs': '0', 'native': True}})
        self.repositorytype = repositorytype
        self.locations = locations
        self.usage = usage
        self.path = path
        self.properties = properties
        self.cloud = cloud
        self.size = size 
