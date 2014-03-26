from core.agility.v3_0.agilitymodel.base.Image import ImageBase
from core.agility.v3_0.agilitymodel.actions.Image import ImageActions

class Image(ImageBase, ImageActions):
    '''
    classdocs
    '''
    def __init__(self, memoryaddsupported=False, resources=[], memoryremovesupported=False, locations=[], imageid=None, cpuremovesupported=False, location=None, mgmtport=None, mgmtprotocol=None, cpuaddsupported=False, credentials=None, cloudtype=None, type=None, properties=[], cloud=None, architecture=None):
        '''
        Constructor
        @param memoryaddsupported: memoryaddsupported
        @type memoryaddsupported: boolean
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param memoryremovesupported: memoryremovesupported
        @type memoryremovesupported: boolean
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param imageid: imageid minOccurs=0
        @type imageid: string
        @param cpuremovesupported: cpuremovesupported
        @type cpuremovesupported: boolean
        @param location: location minOccurs=0
        @type location: string
        @param mgmtport: mgmtport minOccurs=0
        @type mgmtport: int
        @param mgmtprotocol: mgmtprotocol minOccurs=0
        @type mgmtprotocol: string
        @param cpuaddsupported: cpuaddsupported
        @type cpuaddsupported: boolean
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        @param type: type minOccurs=0
        @type type: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        '''
        ImageBase.__init__(self, memoryaddsupported=memoryaddsupported, resources=resources, memoryremovesupported=memoryremovesupported, locations=locations, imageid=imageid, cpuremovesupported=cpuremovesupported, location=location, mgmtport=mgmtport, mgmtprotocol=mgmtprotocol, cpuaddsupported=cpuaddsupported, credentials=credentials, cloudtype=cloudtype, type=type, properties=properties, cloud=cloud, architecture=architecture)
