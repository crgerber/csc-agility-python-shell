from core.agility.v3_3.agilitymodel.base.VolumeStorage import VolumeStorageBase
from core.agility.v3_3.agilitymodel.actions.VolumeStorage import VolumeStorageActions

class VolumeStorage(VolumeStorageBase, VolumeStorageActions):
    '''
    classdocs
    '''
    def __init__(self, volume=None, instance=None, properties=[], size=None, volumesnapshots=[], unit=None, cloud=None, storageid=None, snapshotid=None, device=None, hasfilesystem=None, storage=[], location=None):
        '''
        Constructor
        @param volume: volume minOccurs=0
        @type volume: Link
        @param instance: instance minOccurs=0
        @type instance: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param size: size minOccurs=0
        @type size: int
        @param volumesnapshots: volumesnapshots minOccurs=0 maxOccurs=unbounded
        @type volumesnapshots: Link
        @param unit: unit minOccurs=0
        @type unit: int
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param storageid: storageid minOccurs=0
        @type storageid: string
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: int
        @param device: device minOccurs=0
        @type device: string
        @param hasfilesystem: hasfilesystem minOccurs=0
        @type hasfilesystem: boolean
        @param storage: storage minOccurs=0 maxOccurs=unbounded
        @type storage: Storage
        @param location: location minOccurs=0
        @type location: string
        '''
        VolumeStorageBase.__init__(self, volume=volume, instance=instance, properties=properties, size=size, volumesnapshots=volumesnapshots, unit=unit, cloud=cloud, storageid=storageid, snapshotid=snapshotid, device=device, hasfilesystem=hasfilesystem, storage=storage, location=location)
