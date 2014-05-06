from core.agility.v3_0.agilitymodel.base.Volume import VolumeBase
from core.agility.v3_0.agilitymodel.actions.Volume import VolumeActions

class Volume(VolumeBase, VolumeActions):
    '''
    classdocs
    '''
    def __init__(self, volumestorage=[], credential=None, encrypted=None, raidlevel=None, privatekey=None, volumesize=None, disksize=None, numdisks=None, filesystem=None, cloud=None):
        '''
        Constructor
        @param volumestorage: volumestorage minOccurs=0 maxOccurs=unbounded
        @type volumestorage: Link
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param encrypted: encrypted minOccurs=0
        @type encrypted: boolean
        @param raidlevel: raidlevel minOccurs=0
        @type raidlevel: RaidLevel
        @param privatekey: privatekey minOccurs=0
        @type privatekey: hexBinary
        @param volumesize: volumesize minOccurs=0
        @type volumesize: int
        @param disksize: disksize minOccurs=0
        @type disksize: int
        @param numdisks: numdisks minOccurs=0
        @type numdisks: int
        @param filesystem: filesystem minOccurs=0
        @type filesystem: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        VolumeBase.__init__(self, volumestorage=volumestorage, credential=credential, encrypted=encrypted, raidlevel=raidlevel, privatekey=privatekey, volumesize=volumesize, disksize=disksize, numdisks=numdisks, filesystem=filesystem, cloud=cloud)
