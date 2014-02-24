from base.Snapshot import SnapshotBase
from actions.Snapshot import SnapshotActions

class Snapshot(SnapshotBase, SnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, current=None, snapshotId=None, state=None):
        '''
        Constructor
        @param current: current minOccurs=0
        @type current: boolean
        @param snapshotId: snapshotId minOccurs=0
        @type snapshotId: string
        @param state: state minOccurs=0
        @type state: State
        '''
        SnapshotBase.__init__(self, current=current, snapshotId=snapshotId, state=state)
