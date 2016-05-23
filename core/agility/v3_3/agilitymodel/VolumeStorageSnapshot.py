from core.agility.v3_3.agilitymodel.base.VolumeStorageSnapshot import VolumeStorageSnapshotBase
from core.agility.v3_3.agilitymodel.actions.VolumeStorageSnapshot import VolumeStorageSnapshotActions

class VolumeStorageSnapshot(VolumeStorageSnapshotBase, VolumeStorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, volume=None, cloud=None, status=None, snapshotid=None, storagesnapshots=[], storage=None, progress=None):
        '''
        Constructor
        @param volume: volume minOccurs=0
        @type volume: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param status: status minOccurs=0
        @type status: string
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        @param storagesnapshots: storagesnapshots minOccurs=0 maxOccurs=unbounded
        @type storagesnapshots: Link
        @param storage: storage minOccurs=0
        @type storage: Link
        @param progress: progress minOccurs=0
        @type progress: string
        '''
        VolumeStorageSnapshotBase.__init__(self, volume=volume, cloud=cloud, status=status, snapshotid=snapshotid, storagesnapshots=storagesnapshots, storage=storage, progress=progress)
