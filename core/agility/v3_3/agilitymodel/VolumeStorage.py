from core.agility.v3_3.agilitymodel.base.VolumeStorage import VolumeStorageBase
from core.agility.v3_3.agilitymodel.actions.VolumeStorage import VolumeStorageActions

class VolumeStorage(VolumeStorageBase, VolumeStorageActions):
    '''
    classdocs
    '''
    def __init__(self, location=None, storage=[], properties=[], instance=None, storageid=None, volumesnapshots=[], volume=None, unit=None, size=None, cloud=None, snapshotid=None, hasfilesystem=None, device=None):
        '''
        Constructor
        @param location: location minOccurs=0
        @type location: string
        @param storage: storage minOccurs=0 maxOccurs=unbounded
        @type storage: Storage
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param instance: instance minOccurs=0
        @type instance: Link
        @param storageid: storageid minOccurs=0
        @type storageid: string
        @param volumesnapshots: volumesnapshots minOccurs=0 maxOccurs=unbounded
        @type volumesnapshots: Link
        @param volume: volume minOccurs=0
        @type volume: Link
        @param unit: unit minOccurs=0
        @type unit: int
        @param size: size minOccurs=0
        @type size: int
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: int
        @param hasfilesystem: hasfilesystem minOccurs=0
        @type hasfilesystem: boolean
        @param device: device minOccurs=0
        @type device: string
        '''
        VolumeStorageBase.__init__(self, location=location, storage=storage, properties=properties, instance=instance, storageid=storageid, volumesnapshots=volumesnapshots, volume=volume, unit=unit, size=size, cloud=cloud, snapshotid=snapshotid, hasfilesystem=hasfilesystem, device=device)
