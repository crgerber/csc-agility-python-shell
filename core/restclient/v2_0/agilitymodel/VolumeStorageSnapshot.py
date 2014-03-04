from core.restclient.v2_0.agilitymodel.base.VolumeStorageSnapshot import VolumeStorageSnapshotBase
from core.restclient.v2_0.agilitymodel.actions.VolumeStorageSnapshot import VolumeStorageSnapshotActions

class VolumeStorageSnapshot(VolumeStorageSnapshotBase, VolumeStorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, storage=None, volume=None, storeageSnapshots=list(), progress=None, snapshotId=None, cloud=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param storage: storage minOccurs=0
        @type storage: Link
        @param volume: volume minOccurs=0
        @type volume: Link
        @param storeageSnapshots: storeageSnapshots minOccurs=0 maxOccurs=unbounded
        @type storeageSnapshots: Link
        @param progress: progress minOccurs=0
        @type progress: string
        @param snapshotId: snapshotId minOccurs=0
        @type snapshotId: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        VolumeStorageSnapshotBase.__init__(self, status=status, storage=storage, volume=volume, storeageSnapshots=storeageSnapshots, progress=progress, snapshotId=snapshotId, cloud=cloud)
