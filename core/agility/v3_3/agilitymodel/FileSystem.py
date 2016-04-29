from core.agility.v3_3.agilitymodel.base.FileSystem import FileSystemBase
from core.agility.v3_3.agilitymodel.actions.FileSystem import FileSystemActions

class FileSystem(FileSystemBase, FileSystemActions):
    '''
    classdocs
    '''
    def __init__(self, storagedevices=[], name='', encryptionsupported=None, raidlevels=[], maxvolumesize=''):
        '''
        Constructor
        @param storagedevices: storagedevices minOccurs=0 maxOccurs=unbounded
        @type storagedevices: FileSystemDevice
        @param name: name
        @type name: string
        @param encryptionsupported: encryptionsupported minOccurs=0
        @type encryptionsupported: boolean
        @param raidlevels: raidlevels minOccurs=0 maxOccurs=unbounded
        @type raidlevels: string
        @param maxvolumesize: maxvolumesize
        @type maxvolumesize: string
        '''
        FileSystemBase.__init__(self, storagedevices=storagedevices, name=name, encryptionsupported=encryptionsupported, raidlevels=raidlevels, maxvolumesize=maxvolumesize)
