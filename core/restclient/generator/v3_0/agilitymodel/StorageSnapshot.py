from base.StorageSnapshot import StorageSnapshotBase
from actions.StorageSnapshot import StorageSnapshotActions

class StorageSnapshot(StorageSnapshotBase, StorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, snapshotid=None, storage=None, cloud=None, progress=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        @param storage: storage minOccurs=0
        @type storage: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param progress: progress minOccurs=0
        @type progress: string
        '''
        StorageSnapshotBase.__init__(self, status=status, snapshotid=snapshotid, storage=storage, cloud=cloud, progress=progress)
