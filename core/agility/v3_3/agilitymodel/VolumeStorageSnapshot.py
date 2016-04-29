from core.agility.v3_3.agilitymodel.base.VolumeStorageSnapshot import VolumeStorageSnapshotBase
from core.agility.v3_3.agilitymodel.actions.VolumeStorageSnapshot import VolumeStorageSnapshotActions

class VolumeStorageSnapshot(VolumeStorageSnapshotBase, VolumeStorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, storagesnapshots=[], progress=None, snapshotid=None, cloud=None, storage=None, status=None, volume=None):
        '''
        Constructor
        @param storagesnapshots: storagesnapshots minOccurs=0 maxOccurs=unbounded
        @type storagesnapshots: Link
        @param progress: progress minOccurs=0
        @type progress: string
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param storage: storage minOccurs=0
        @type storage: Link
        @param status: status minOccurs=0
        @type status: string
        @param volume: volume minOccurs=0
        @type volume: Link
        '''
        VolumeStorageSnapshotBase.__init__(self, storagesnapshots=storagesnapshots, progress=progress, snapshotid=snapshotid, cloud=cloud, storage=storage, status=status, volume=volume)
