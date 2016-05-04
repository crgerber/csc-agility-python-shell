from base.VolumeStorageSnapshot import VolumeStorageSnapshotBase
from actions.VolumeStorageSnapshot import VolumeStorageSnapshotActions

class VolumeStorageSnapshot(VolumeStorageSnapshotBase, VolumeStorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, storagesnapshots=[], storage=None, volume=None, progress=None, snapshotid=None, cloud=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param storagesnapshots: storagesnapshots minOccurs=0 maxOccurs=unbounded
        @type storagesnapshots: Link
        @param storage: storage minOccurs=0
        @type storage: Link
        @param volume: volume minOccurs=0
        @type volume: Link
        @param progress: progress minOccurs=0
        @type progress: string
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        VolumeStorageSnapshotBase.__init__(self, status=status, storagesnapshots=storagesnapshots, storage=storage, volume=volume, progress=progress, snapshotid=snapshotid, cloud=cloud)
