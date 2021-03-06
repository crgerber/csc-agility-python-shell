from base.Storage import StorageBase
from actions.Storage import StorageActions

class Storage(StorageBase, StorageActions):
    '''
    classdocs
    '''
    def __init__(self, location=None, snapshots=[], volume=None, instance=None, unit=None, storageid=None, device=None, snapshotid=None, cloud=None, size=None):
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
        @param storageid: storageid minOccurs=0
        @type storageid: string
        @param device: device minOccurs=0
        @type device: string
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: int
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param size: size minOccurs=0
        @type size: int
        '''
        StorageBase.__init__(self, location=location, snapshots=snapshots, volume=volume, instance=instance, unit=unit, storageid=storageid, device=device, snapshotid=snapshotid, cloud=cloud, size=size)
