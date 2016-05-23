from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ImageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, cpuremovesupported=False, credentials=None, memoryaddsupported=False, properties=[], cpuaddsupported=False, locations=[], cloudtype=None, imageid=None, cloud=None, mgmtprotocol=None, mgmtport=None, resources=[], architecture=None, memoryremovesupported=False, flagssynced=False, type=None, location=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cpuRemoveSupported': {'name': 'cpuremovesupported', 'native': True, 'type': 'boolean'}, 'cloudType': {'name': 'cloudtype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'location': {'name': 'location', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'cpuAddSupported': {'name': 'cpuaddsupported', 'native': True, 'type': 'boolean'}, 'locations': {'name': 'locations', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'credentials': {'name': 'credentials', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'imageId': {'name': 'imageid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'mgmtProtocol': {'name': 'mgmtprotocol', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'mgmtPort': {'name': 'mgmtport', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Resource'}, 'architecture': {'name': 'architecture', 'minOccurs': '0', 'native': False, 'type': 'Architecture'}, 'memoryRemoveSupported': {'name': 'memoryremovesupported', 'native': True, 'type': 'boolean'}, 'flagsSynced': {'name': 'flagssynced', 'native': True, 'type': 'boolean'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'memoryAddSupported': {'name': 'memoryaddsupported', 'native': True, 'type': 'boolean'}})
        self.cpuremovesupported = cpuremovesupported
        self.credentials = credentials
        self.memoryaddsupported = memoryaddsupported
        self.properties = properties
        self.cpuaddsupported = cpuaddsupported
        self.locations = locations
        self.cloudtype = cloudtype
        self.imageid = imageid
        self.cloud = cloud
        self.mgmtprotocol = mgmtprotocol
        self.mgmtport = mgmtport
        self.resources = resources
        self.architecture = architecture
        self.memoryremovesupported = memoryremovesupported
        self.flagssynced = flagssynced
        self.type = type
        self.location = location 
