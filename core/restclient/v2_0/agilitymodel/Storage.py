from core.restclient.v2_0.agilitymodel.base.Storage import StorageBase
from core.restclient.v2_0.agilitymodel.actions.Storage import StorageActions

class Storage(StorageBase, StorageActions):
    '''
    classdocs
    '''
    def __init__(self, location=None, snapshots=list(), volume=None, instance=None, unit=None, storageId=None, device=None, snapshotId=None, cloud=None, size=None):
        '''
        Constructor
        @param location: location minOccurs=0
        @type location: string
        @param snapshots: snapshots minOccurs=0 maxOccurs=unbounded
        @type snapshots: Link
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
        StorageBase.__init__(self, location=location, snapshots=snapshots, volume=volume, instance=instance, unit=unit, storageId=storageId, device=device, snapshotId=snapshotId, cloud=cloud, size=size)
