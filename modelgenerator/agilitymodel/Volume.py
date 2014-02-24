from base.Volume import VolumeBase
from actions.Volume import VolumeActions

class Volume(VolumeBase, VolumeActions):
    '''
    classdocs
    '''
    def __init__(self, volumeStorage=list(), credential=None, encrypted=None, raidLevel=None, privateKey=None, volumeSize=None, diskSize=None, numDisks=None, fileSystem=None, cloud=None):
        '''
        Constructor
        @param volumeStorage: volumeStorage minOccurs=0 maxOccurs=unbounded
        @type volumeStorage: Link
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param encrypted: encrypted minOccurs=0
        @type encrypted: boolean
        @param raidLevel: raidLevel minOccurs=0
        @type raidLevel: RaidLevel
        @param privateKey: privateKey minOccurs=0
        @type privateKey: hexBinary
        @param volumeSize: volumeSize minOccurs=0
        @type volumeSize: int
        @param diskSize: diskSize minOccurs=0
        @type diskSize: int
        @param numDisks: numDisks minOccurs=0
        @type numDisks: int
        @param fileSystem: fileSystem minOccurs=0
        @type fileSystem: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        VolumeBase.__init__(self, volumeStorage=volumeStorage, credential=credential, encrypted=encrypted, raidLevel=raidLevel, privateKey=privateKey, volumeSize=volumeSize, diskSize=diskSize, numDisks=numDisks, fileSystem=fileSystem, cloud=cloud)
