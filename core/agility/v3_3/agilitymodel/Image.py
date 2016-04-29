from core.agility.v3_3.agilitymodel.base.Image import ImageBase
from core.agility.v3_3.agilitymodel.actions.Image import ImageActions

class Image(ImageBase, ImageActions):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, location=None, properties=[], resources=[], cloudtype=None, mgmtport=None, cpuremovesupported=False, memoryaddsupported=False, type=None, flagssynced=False, mgmtprotocol=None, cloud=None, memoryremovesupported=False, locations=[], architecture=None, cpuaddsupported=False, imageid=None):
        '''
        Constructor
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param location: location minOccurs=0
        @type location: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        @param mgmtport: mgmtport minOccurs=0
        @type mgmtport: int
        @param cpuremovesupported: cpuremovesupported
        @type cpuremovesupported: boolean
        @param memoryaddsupported: memoryaddsupported
        @type memoryaddsupported: boolean
        @param type: type minOccurs=0
        @type type: string
        @param flagssynced: flagssynced
        @type flagssynced: boolean
        @param mgmtprotocol: mgmtprotocol minOccurs=0
        @type mgmtprotocol: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param memoryremovesupported: memoryremovesupported
        @type memoryremovesupported: boolean
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        @param cpuaddsupported: cpuaddsupported
        @type cpuaddsupported: boolean
        @param imageid: imageid minOccurs=0
        @type imageid: string
        '''
        ImageBase.__init__(self, credentials=credentials, location=location, properties=properties, resources=resources, cloudtype=cloudtype, mgmtport=mgmtport, cpuremovesupported=cpuremovesupported, memoryaddsupported=memoryaddsupported, type=type, flagssynced=flagssynced, mgmtprotocol=mgmtprotocol, cloud=cloud, memoryremovesupported=memoryremovesupported, locations=locations, architecture=architecture, cpuaddsupported=cpuaddsupported, imageid=imageid)
