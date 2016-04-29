from .base.FileSystem import FileSystemBase
from .actions.FileSystem import FileSystemActions

class FileSystem(FileSystemBase, FileSystemActions):
    '''
    classdocs
    '''
    def __init__(self, storagedevices=[], encryptionsupported=None, name='', raidlevels=[]):
        '''
        Constructor
        @param storagedevices: storagedevices minOccurs=0 maxOccurs=unbounded
        @type storagedevices: FileSystemDevice
        @param encryptionsupported: encryptionsupported minOccurs=0
        @type encryptionsupported: boolean
        @param name: name
        @type name: string
        @param raidlevels: raidlevels minOccurs=0 maxOccurs=unbounded
        @type raidlevels: string
        '''
        FileSystemBase.__init__(self, storagedevices=storagedevices, encryptionsupported=encryptionsupported, name=name, raidlevels=raidlevels)
