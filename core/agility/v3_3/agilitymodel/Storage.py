from core.agility.v3_3.agilitymodel.base.Storage import StorageBase
from core.agility.v3_3.agilitymodel.actions.Storage import StorageActions

class Storage(StorageBase, StorageActions):
    '''
    classdocs
    '''
    def __init__(self, location=None, unit=None, device=None, size=None, snapshotid=None, snapshots=[], cloud=None, storageid=None, instance=None, volume=None, properties=[]):
        '''
        Constructor
        @param location: location minOccurs=0
        @type location: string
        @param unit: unit minOccurs=0
        @type unit: int
        @param device: device minOccurs=0
        @type device: string
        @param size: size minOccurs=0
        @type size: int
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: int
        @param snapshots: snapshots minOccurs=0 maxOccurs=unbounded
        @type snapshots: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param storageid: storageid minOccurs=0
        @type storageid: string
        @param instance: instance minOccurs=0
        @type instance: Link
        @param volume: volume minOccurs=0
        @type volume: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        StorageBase.__init__(self, location=location, unit=unit, device=device, size=size, snapshotid=snapshotid, snapshots=snapshots, cloud=cloud, storageid=storageid, instance=instance, volume=volume, properties=properties)
