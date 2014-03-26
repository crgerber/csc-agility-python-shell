from base.FileSystemDevice import FileSystemDeviceBase
from actions.FileSystemDevice import FileSystemDeviceActions

class FileSystemDevice(FileSystemDeviceBase, FileSystemDeviceActions):
    '''
    classdocs
    '''
    def __init__(self, device=None, cloudtype=None):
        '''
        Constructor
        @param device: device minOccurs=0
        @type device: string
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        '''
        FileSystemDeviceBase.__init__(self, device=device, cloudtype=cloudtype)
