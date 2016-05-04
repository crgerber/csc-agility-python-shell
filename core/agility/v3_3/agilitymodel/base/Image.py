from Asset import AssetBase

class ImageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, memoryaddsupported=False, flagssynced=False, resources=[], memoryremovesupported=False, locations=[], imageid=None, cpuremovesupported=False, location=None, mgmtport=None, mgmtprotocol=None, cpuaddsupported=False, credentials=None, cloudtype=None, type=None, properties=[], cloud=None, architecture=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'mgmtPort': {'type': 'int', 'name': 'mgmtport', 'minOccurs': '0', 'native': True}, 'flagsSynced': {'type': 'boolean', 'name': 'flagssynced', 'native': True}, 'memoryRemoveSupported': {'type': 'boolean', 'name': 'memoryremovesupported', 'native': True}, 'locations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'locations', 'minOccurs': '0', 'native': False}, 'imageId': {'type': 'string', 'name': 'imageid', 'minOccurs': '0', 'native': True}, 'architecture': {'type': 'Architecture', 'name': 'architecture', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'cpuRemoveSupported': {'type': 'boolean', 'name': 'cpuremovesupported', 'native': True}, 'memoryAddSupported': {'type': 'boolean', 'name': 'memoryaddsupported', 'native': True}, 'mgmtProtocol': {'type': 'string', 'name': 'mgmtprotocol', 'minOccurs': '0', 'native': True}, 'cpuAddSupported': {'type': 'boolean', 'name': 'cpuaddsupported', 'native': True}, 'credentials': {'type': 'Credential', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'cloudType': {'type': 'Link', 'name': 'cloudtype', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}})
        self.memoryaddsupported = memoryaddsupported
        self.flagssynced = flagssynced
        self.resources = resources
        self.memoryremovesupported = memoryremovesupported
        self.locations = locations
        self.imageid = imageid
        self.cpuremovesupported = cpuremovesupported
        self.location = location
        self.mgmtport = mgmtport
        self.mgmtprotocol = mgmtprotocol
        self.cpuaddsupported = cpuaddsupported
        self.credentials = credentials
        self.cloudtype = cloudtype
        self.type = type
        self.properties = properties
        self.cloud = cloud
        self.architecture = architecture 
