from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, disksize=None, volumestorage=[], privatekey=None, volumesize=None, raidlevel=None, credential=None, numdisks=None, filesystem=None, encrypted=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'volumeStorage': {'name': 'volumestorage', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'privateKey': {'name': 'privatekey', 'minOccurs': '0', 'native': True, 'type': 'hexBinary'}, 'diskSize': {'name': 'disksize', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'raidLevel': {'name': 'raidlevel', 'minOccurs': '0', 'native': False, 'type': 'RaidLevel'}, 'encrypted': {'name': 'encrypted', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'numDisks': {'name': 'numdisks', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'fileSystem': {'name': 'filesystem', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'volumeSize': {'name': 'volumesize', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'credential': {'name': 'credential', 'minOccurs': '0', 'native': False, 'type': 'Credential'}})
        self.cloud = cloud
        self.disksize = disksize
        self.volumestorage = volumestorage
        self.privatekey = privatekey
        self.volumesize = volumesize
        self.raidlevel = raidlevel
        self.credential = credential
        self.numdisks = numdisks
        self.filesystem = filesystem
        self.encrypted = encrypted 
