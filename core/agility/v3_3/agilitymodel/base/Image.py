from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ImageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, location=None, properties=[], resources=[], cloudtype=None, mgmtport=None, cpuremovesupported=False, memoryaddsupported=False, type=None, flagssynced=False, mgmtprotocol=None, cloud=None, memoryremovesupported=False, locations=[], architecture=None, cpuaddsupported=False, imageid=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentials': {'native': False, 'name': 'credentials', 'minOccurs': '0', 'type': 'Credential'}, 'location': {'native': True, 'name': 'location', 'minOccurs': '0', 'type': 'string'}, 'imageId': {'native': True, 'name': 'imageid', 'minOccurs': '0', 'type': 'string'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'Resource'}, 'cloudType': {'native': False, 'name': 'cloudtype', 'minOccurs': '0', 'type': 'Link'}, 'mgmtPort': {'native': True, 'name': 'mgmtport', 'minOccurs': '0', 'type': 'int'}, 'cpuRemoveSupported': {'native': True, 'name': 'cpuremovesupported', 'type': 'boolean'}, 'memoryAddSupported': {'native': True, 'name': 'memoryaddsupported', 'type': 'boolean'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}, 'flagsSynced': {'native': True, 'name': 'flagssynced', 'type': 'boolean'}, 'mgmtProtocol': {'native': True, 'name': 'mgmtprotocol', 'minOccurs': '0', 'type': 'string'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'memoryRemoveSupported': {'native': True, 'name': 'memoryremovesupported', 'type': 'boolean'}, 'locations': {'maxOccurs': 'unbounded', 'native': False, 'name': 'locations', 'minOccurs': '0', 'type': 'Link'}, 'architecture': {'native': False, 'name': 'architecture', 'minOccurs': '0', 'type': 'Architecture'}, 'cpuAddSupported': {'native': True, 'name': 'cpuaddsupported', 'type': 'boolean'}})
        self.credentials = credentials
        self.location = location
        self.properties = properties
        self.resources = resources
        self.cloudtype = cloudtype
        self.mgmtport = mgmtport
        self.cpuremovesupported = cpuremovesupported
        self.memoryaddsupported = memoryaddsupported
        self.type = type
        self.flagssynced = flagssynced
        self.mgmtprotocol = mgmtprotocol
        self.cloud = cloud
        self.memoryremovesupported = memoryremovesupported
        self.locations = locations
        self.architecture = architecture
        self.cpuaddsupported = cpuaddsupported
        self.imageid = imageid 
