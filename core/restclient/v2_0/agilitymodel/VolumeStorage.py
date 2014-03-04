from core.restclient.v2_0.agilitymodel.base.VolumeStorage import VolumeStorageBase
from core.restclient.v2_0.agilitymodel.actions.VolumeStorage import VolumeStorageActions

class VolumeStorage(VolumeStorageBase, VolumeStorageActions):
    '''
    classdocs
    '''
    def __init__(self, hasFileSystem=None, volumeSnapshots=list(), storage=list(), location=None, volume=None, instance=None, unit=None, storageId=None, device=None, snapshotId=None, cloud=None, size=None):
        '''
        Constructor
        @param hasFileSystem: hasFileSystem minOccurs=0
        @type hasFileSystem: boolean
        @param volumeSnapshots: volumeSnapshots minOccurs=0 maxOccurs=unbounded
        @type volumeSnapshots: Link
        @param storage: storage minOccurs=0 maxOccurs=unbounded
        @type storage: Link
        @param location: location minOccurs=0
        @type location: string
        @param volume: volume minOccurs=0
        @type volume: Link
        @param instance: instance minOccurs=0
        @type instance: Link
        @param unit: unit minOccurs=0
        @type unit: int
        @param storageId: storageId minOccurs=0
        @type storageId: string
        @param device: device minOccurs=0
        @type device: string
        @param snapshotId: snapshotId minOccurs=0
        @type snapshotId: int
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param size: size minOccurs=0
        @type size: int
        '''
        VolumeStorageBase.__init__(self, hasFileSystem=hasFileSystem, volumeSnapshots=volumeSnapshots, storage=storage, location=location, volume=volume, instance=instance, unit=unit, storageId=storageId, device=device, snapshotId=snapshotId, cloud=cloud, size=size)
