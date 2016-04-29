from .base.Snapshot import SnapshotBase
from .actions.Snapshot import SnapshotActions

class Snapshot(SnapshotBase, SnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, current=None, snapshotid=None, state=None, instance=None):
        '''
        Constructor
        @param current: current minOccurs=0
        @type current: boolean
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        @param state: state minOccurs=0
        @type state: State
        @param instance: instance minOccurs=0
        @type instance: Link
        '''
        SnapshotBase.__init__(self, current=current, snapshotid=snapshotid, state=state, instance=instance)
