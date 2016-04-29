from core.agility.v3_3.agilitymodel.base.FileSystemDevice import FileSystemDeviceBase
from core.agility.v3_3.agilitymodel.actions.FileSystemDevice import FileSystemDeviceActions

class FileSystemDevice(FileSystemDeviceBase, FileSystemDeviceActions):
    '''
    classdocs
    '''
    def __init__(self, cloudtype=None, device=None):
        '''
        Constructor
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        @param device: device minOccurs=0
        @type device: string
        '''
        FileSystemDeviceBase.__init__(self, cloudtype=cloudtype, device=device)
