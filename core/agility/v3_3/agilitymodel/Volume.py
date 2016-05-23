from core.agility.v3_3.agilitymodel.base.Volume import VolumeBase
from core.agility.v3_3.agilitymodel.actions.Volume import VolumeActions

class Volume(VolumeBase, VolumeActions):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, disksize=None, volumestorage=[], privatekey=None, volumesize=None, raidlevel=None, credential=None, numdisks=None, filesystem=None, encrypted=None):
        '''
        Constructor
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param disksize: disksize minOccurs=0
        @type disksize: int
        @param volumestorage: volumestorage minOccurs=0 maxOccurs=unbounded
        @type volumestorage: Link
        @param privatekey: privatekey minOccurs=0
        @type privatekey: hexBinary
        @param volumesize: volumesize minOccurs=0
        @type volumesize: int
        @param raidlevel: raidlevel minOccurs=0
        @type raidlevel: RaidLevel
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param numdisks: numdisks minOccurs=0
        @type numdisks: int
        @param filesystem: filesystem minOccurs=0
        @type filesystem: string
        @param encrypted: encrypted minOccurs=0
        @type encrypted: boolean
        '''
        VolumeBase.__init__(self, cloud=cloud, disksize=disksize, volumestorage=volumestorage, privatekey=privatekey, volumesize=volumesize, raidlevel=raidlevel, credential=credential, numdisks=numdisks, filesystem=filesystem, encrypted=encrypted)
