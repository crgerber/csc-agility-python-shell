from core.agility.v3_3.agilitymodel.base.Volume import VolumeBase
from core.agility.v3_3.agilitymodel.actions.Volume import VolumeActions

class Volume(VolumeBase, VolumeActions):
    '''
    classdocs
    '''
    def __init__(self, encrypted=None, volumesize=None, credential=None, disksize=None, filesystem=None, privatekey=None, cloud=None, volumestorage=[], numdisks=None, raidlevel=None):
        '''
        Constructor
        @param encrypted: encrypted minOccurs=0
        @type encrypted: boolean
        @param volumesize: volumesize minOccurs=0
        @type volumesize: int
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param disksize: disksize minOccurs=0
        @type disksize: int
        @param filesystem: filesystem minOccurs=0
        @type filesystem: string
        @param privatekey: privatekey minOccurs=0
        @type privatekey: hexBinary
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param volumestorage: volumestorage minOccurs=0 maxOccurs=unbounded
        @type volumestorage: Link
        @param numdisks: numdisks minOccurs=0
        @type numdisks: int
        @param raidlevel: raidlevel minOccurs=0
        @type raidlevel: RaidLevel
        '''
        VolumeBase.__init__(self, encrypted=encrypted, volumesize=volumesize, credential=credential, disksize=disksize, filesystem=filesystem, privatekey=privatekey, cloud=cloud, volumestorage=volumestorage, numdisks=numdisks, raidlevel=raidlevel)
