from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, encrypted=None, volumesize=None, credential=None, disksize=None, filesystem=None, privatekey=None, cloud=None, volumestorage=[], numdisks=None, raidlevel=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'encrypted': {'native': True, 'name': 'encrypted', 'minOccurs': '0', 'type': 'boolean'}, 'volumeSize': {'native': True, 'name': 'volumesize', 'minOccurs': '0', 'type': 'int'}, 'privateKey': {'native': True, 'name': 'privatekey', 'minOccurs': '0', 'type': 'hexBinary'}, 'diskSize': {'native': True, 'name': 'disksize', 'minOccurs': '0', 'type': 'int'}, 'fileSystem': {'native': True, 'name': 'filesystem', 'minOccurs': '0', 'type': 'string'}, 'credential': {'native': False, 'name': 'credential', 'minOccurs': '0', 'type': 'Credential'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'volumeStorage': {'maxOccurs': 'unbounded', 'native': False, 'name': 'volumestorage', 'minOccurs': '0', 'type': 'Link'}, 'numDisks': {'native': True, 'name': 'numdisks', 'minOccurs': '0', 'type': 'int'}, 'raidLevel': {'native': False, 'name': 'raidlevel', 'minOccurs': '0', 'type': 'RaidLevel'}})
        self.encrypted = encrypted
        self.volumesize = volumesize
        self.credential = credential
        self.disksize = disksize
        self.filesystem = filesystem
        self.privatekey = privatekey
        self.cloud = cloud
        self.volumestorage = volumestorage
        self.numdisks = numdisks
        self.raidlevel = raidlevel 
