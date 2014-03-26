from core.agility.v2_0.agilitymodel.base.FileSystem import FileSystemBase
from core.agility.v2_0.agilitymodel.actions.FileSystem import FileSystemActions

class FileSystem(FileSystemBase, FileSystemActions):
    '''
    classdocs
    '''
    def __init__(self, storageDevices=list(), encryptionSupported=None, name='', raidLevels=list()):
        '''
        Constructor
        @param storageDevices: storageDevices minOccurs=0 maxOccurs=unbounded
        @type storageDevices: FileSystemDevice
        @param encryptionSupported: encryptionSupported minOccurs=0
        @type encryptionSupported: boolean
        @param name: name
        @type name: string
        @param raidLevels: raidLevels minOccurs=0 maxOccurs=unbounded
        @type raidLevels: string
        '''
        FileSystemBase.__init__(self, storageDevices=storageDevices, encryptionSupported=encryptionSupported, name=name, raidLevels=raidLevels)
