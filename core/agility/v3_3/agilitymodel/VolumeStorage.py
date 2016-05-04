from base.VolumeStorage import VolumeStorageBase
from actions.VolumeStorage import VolumeStorageActions

class VolumeStorage(VolumeStorageBase, VolumeStorageActions):
    '''
    classdocs
    '''
    def __init__(self, hasfilesystem=None, volumesnapshots=[], storage=[], location=None, volume=None, instance=None, unit=None, storageid=None, device=None, snapshotid=None, properties=[], cloud=None, size=None):
        '''
        Constructor
        @param hasfilesystem: hasfilesystem minOccurs=0
        @type hasfilesystem: boolean
        @param volumesnapshots: volumesnapshots minOccurs=0 maxOccurs=unbounded
        @type volumesnapshots: Link
        @param storage: storage minOccurs=0 maxOccurs=unbounded
        @type storage: Storage
        @param location: location minOccurs=0
        @type location: string
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
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param size: size minOccurs=0
        @type size: int
        '''
        VolumeStorageBase.__init__(self, hasfilesystem=hasfilesystem, volumesnapshots=volumesnapshots, storage=storage, location=location, volume=volume, instance=instance, unit=unit, storageid=storageid, device=device, snapshotid=snapshotid, properties=properties, cloud=cloud, size=size)
