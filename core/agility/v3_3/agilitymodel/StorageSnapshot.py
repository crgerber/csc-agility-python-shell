from core.agility.v3_3.agilitymodel.base.StorageSnapshot import StorageSnapshotBase
from core.agility.v3_3.agilitymodel.actions.StorageSnapshot import StorageSnapshotActions

class StorageSnapshot(StorageSnapshotBase, StorageSnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, progress=None, cloud=None, storage=None, status=None, snapshotid=None):
        '''
        Constructor
        @param progress: progress minOccurs=0
        @type progress: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param storage: storage minOccurs=0
        @type storage: Link
        @param status: status minOccurs=0
        @type status: string
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        '''
        StorageSnapshotBase.__init__(self, progress=progress, cloud=cloud, storage=storage, status=status, snapshotid=snapshotid)
