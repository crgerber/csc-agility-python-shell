from core.agility.v3_3.agilitymodel.base.Storage import StorageBase
from core.agility.v3_3.agilitymodel.actions.Storage import StorageActions

class Storage(StorageBase, StorageActions):
    '''
    classdocs
    '''
    def __init__(self, volume=None, cloud=None, instance=None, properties=[], storageid=None, snapshots=[], snapshotid=None, size=None, device=None, unit=None, location=None):
        '''
        Constructor
        @param volume: volume minOccurs=0
        @type volume: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param instance: instance minOccurs=0
        @type instance: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param storageid: storageid minOccurs=0
        @type storageid: string
        @param snapshots: snapshots minOccurs=0 maxOccurs=unbounded
        @type snapshots: Link
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: int
        @param size: size minOccurs=0
        @type size: int
        @param device: device minOccurs=0
        @type device: string
        @param unit: unit minOccurs=0
        @type unit: int
        @param location: location minOccurs=0
        @type location: string
        '''
        StorageBase.__init__(self, volume=volume, cloud=cloud, instance=instance, properties=properties, storageid=storageid, snapshots=snapshots, snapshotid=snapshotid, size=size, device=device, unit=unit, location=location)
