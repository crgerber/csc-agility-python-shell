from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class VolumeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, volumeStorage=list(), credential=None, encrypted=None, raidLevel=None, privateKey=None, volumeSize=None, diskSize=None, numDisks=None, fileSystem=None, cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'volumeStorage': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumeStorage', 'minOccurs': '0', 'native': False}, 'credential': {'type': 'Credential', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'encrypted': {'type': 'boolean', 'name': 'encrypted', 'minOccurs': '0', 'native': True}, 'raidLevel': {'type': 'RaidLevel', 'name': 'raidLevel', 'minOccurs': '0', 'native': False}, 'privateKey': {'type': 'hexBinary', 'name': 'privateKey', 'minOccurs': '0', 'native': True}, 'volumeSize': {'type': 'int', 'name': 'volumeSize', 'minOccurs': '0', 'native': True}, 'diskSize': {'type': 'int', 'name': 'diskSize', 'minOccurs': '0', 'native': True}, 'numDisks': {'type': 'int', 'name': 'numDisks', 'minOccurs': '0', 'native': True}, 'fileSystem': {'type': 'string', 'name': 'fileSystem', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.volumeStorage = volumeStorage
        self.credential = credential
        self.encrypted = encrypted
        self.raidLevel = raidLevel
        self.privateKey = privateKey
        self.volumeSize = volumeSize
        self.diskSize = diskSize
        self.numDisks = numDisks
        self.fileSystem = fileSystem
        self.cloud = cloud 
