from core.agility.v3_3.agilitymodel.base.Image import ImageBase
from core.agility.v3_3.agilitymodel.actions.Image import ImageActions

class Image(ImageBase, ImageActions):
    '''
    classdocs
    '''
    def __init__(self, cpuremovesupported=False, credentials=None, memoryaddsupported=False, properties=[], cpuaddsupported=False, locations=[], cloudtype=None, imageid=None, cloud=None, mgmtprotocol=None, mgmtport=None, resources=[], architecture=None, memoryremovesupported=False, flagssynced=False, type=None, location=None):
        '''
        Constructor
        @param cpuremovesupported: cpuremovesupported
        @type cpuremovesupported: boolean
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param memoryaddsupported: memoryaddsupported
        @type memoryaddsupported: boolean
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param cpuaddsupported: cpuaddsupported
        @type cpuaddsupported: boolean
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        @param imageid: imageid minOccurs=0
        @type imageid: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param mgmtprotocol: mgmtprotocol minOccurs=0
        @type mgmtprotocol: string
        @param mgmtport: mgmtport minOccurs=0
        @type mgmtport: int
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        @param memoryremovesupported: memoryremovesupported
        @type memoryremovesupported: boolean
        @param flagssynced: flagssynced
        @type flagssynced: boolean
        @param type: type minOccurs=0
        @type type: string
        @param location: location minOccurs=0
        @type location: string
        '''
        ImageBase.__init__(self, cpuremovesupported=cpuremovesupported, credentials=credentials, memoryaddsupported=memoryaddsupported, properties=properties, cpuaddsupported=cpuaddsupported, locations=locations, cloudtype=cloudtype, imageid=imageid, cloud=cloud, mgmtprotocol=mgmtprotocol, mgmtport=mgmtport, resources=resources, architecture=architecture, memoryremovesupported=memoryremovesupported, flagssynced=flagssynced, type=type, location=location)
