from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, volumestorage=[], credential=None, encrypted=None, raidlevel=None, privatekey=None, volumesize=None, disksize=None, numdisks=None, filesystem=None, cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'volumeStorage': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumestorage', 'minOccurs': '0', 'native': False}, 'credential': {'type': 'Credential', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'encrypted': {'type': 'boolean', 'name': 'encrypted', 'minOccurs': '0', 'native': True}, 'raidLevel': {'type': 'RaidLevel', 'name': 'raidlevel', 'minOccurs': '0', 'native': False}, 'privateKey': {'type': 'hexBinary', 'name': 'privatekey', 'minOccurs': '0', 'native': True}, 'volumeSize': {'type': 'int', 'name': 'volumesize', 'minOccurs': '0', 'native': True}, 'diskSize': {'type': 'int', 'name': 'disksize', 'minOccurs': '0', 'native': True}, 'numDisks': {'type': 'int', 'name': 'numdisks', 'minOccurs': '0', 'native': True}, 'fileSystem': {'type': 'string', 'name': 'filesystem', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.volumestorage = volumestorage
        self.credential = credential
        self.encrypted = encrypted
        self.raidlevel = raidlevel
        self.privatekey = privatekey
        self.volumesize = volumesize
        self.disksize = disksize
        self.numdisks = numdisks
        self.filesystem = filesystem
        self.cloud = cloud 
