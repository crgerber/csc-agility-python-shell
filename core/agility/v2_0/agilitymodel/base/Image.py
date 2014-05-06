from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class ImageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, resources=list(), imageId=None, location=None, credentials=None, cloudType=None, type=None, cloud=None, architecture=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'imageId': {'type': 'string', 'name': 'imageId', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}, 'credentials': {'type': 'Credential', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'cloudType': {'type': 'Link', 'name': 'cloudType', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'architecture': {'type': 'Architecture', 'name': 'architecture', 'minOccurs': '0', 'native': False}})
        self.resources = resources
        self.imageId = imageId
        self.location = location
        self.credentials = credentials
        self.cloudType = cloudType
        self.type = type
        self.cloud = cloud
        self.architecture = architecture 
