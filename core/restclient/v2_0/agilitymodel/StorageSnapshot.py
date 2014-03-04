from core.restclient.v2_0.agilitymodel.base.StorageSnapshot import StorageSnapshotBase
from core.restclient.v2_0.agilitymodel.actions.StorageSnapshot import StorageSnapshotActions

class StorageSnapshot(StorageSnapshotBase, StorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, snapshotId=None, storage=None, cloud=None, progress=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param snapshotId: snapshotId minOccurs=0
        @type snapshotId: string
        @param storage: storage minOccurs=0
        @type storage: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param progress: progress minOccurs=0
        @type progress: string
        '''
        StorageSnapshotBase.__init__(self, status=status, snapshotId=snapshotId, storage=storage, cloud=cloud, progress=progress)
