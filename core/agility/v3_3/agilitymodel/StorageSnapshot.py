from core.agility.v3_3.agilitymodel.base.StorageSnapshot import StorageSnapshotBase
from core.agility.v3_3.agilitymodel.actions.StorageSnapshot import StorageSnapshotActions

class StorageSnapshot(StorageSnapshotBase, StorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, snapshotid=None, cloud=None, status=None, storage=None, progress=None):
        '''
        Constructor
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param status: status minOccurs=0
        @type status: string
        @param storage: storage minOccurs=0
        @type storage: Link
        @param progress: progress minOccurs=0
        @type progress: string
        '''
        StorageSnapshotBase.__init__(self, snapshotid=snapshotid, cloud=cloud, status=status, storage=storage, progress=progress)
