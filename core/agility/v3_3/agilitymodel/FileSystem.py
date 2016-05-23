from core.agility.v3_3.agilitymodel.base.FileSystem import FileSystemBase
from core.agility.v3_3.agilitymodel.actions.FileSystem import FileSystemActions

class FileSystem(FileSystemBase, FileSystemActions):
    '''
    classdocs
    '''
    def __init__(self, name='', maxvolumesize='', encryptionsupported=None, storagedevices=[], raidlevels=[]):
        '''
        Constructor
        @param name: name
        @type name: string
        @param maxvolumesize: maxvolumesize
        @type maxvolumesize: string
        @param encryptionsupported: encryptionsupported minOccurs=0
        @type encryptionsupported: boolean
        @param storagedevices: storagedevices minOccurs=0 maxOccurs=unbounded
        @type storagedevices: FileSystemDevice
        @param raidlevels: raidlevels minOccurs=0 maxOccurs=unbounded
        @type raidlevels: string
        '''
        FileSystemBase.__init__(self, name=name, maxvolumesize=maxvolumesize, encryptionsupported=encryptionsupported, storagedevices=storagedevices, raidlevels=raidlevels)
