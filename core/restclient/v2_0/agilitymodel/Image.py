from core.restclient.v2_0.agilitymodel.base.Image import ImageBase
from core.restclient.v2_0.agilitymodel.actions.Image import ImageActions

class Image(ImageBase, ImageActions):
    '''
    classdocs
    '''
    def __init__(self, resources=list(), imageId=None, location=None, credentials=None, cloudType=None, type=None, cloud=None, architecture=None):
        '''
        Constructor
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param imageId: imageId minOccurs=0
        @type imageId: string
        @param location: location minOccurs=0
        @type location: string
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param cloudType: cloudType minOccurs=0
        @type cloudType: Link
        @param type: type minOccurs=0
        @type type: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        '''
        ImageBase.__init__(self, resources=resources, imageId=imageId, location=location, credentials=credentials, cloudType=cloudType, type=type, cloud=cloud, architecture=architecture)
