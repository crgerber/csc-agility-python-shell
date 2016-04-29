from core.agility.v3_3.agilitymodel.base.Snapshot import SnapshotBase
from core.agility.v3_3.agilitymodel.actions.Snapshot import SnapshotActions

class Snapshot(SnapshotBase, SnapshotActions):
    '''
    classdocs
    '''
    def __init__(self, instance=None, snapshotid=None, current=None, state=None):
        '''
        Constructor
        @param instance: instance minOccurs=0
        @type instance: Link
        @param snapshotid: snapshotid minOccurs=0
        @type snapshotid: string
        @param current: current minOccurs=0
        @type current: boolean
        @param state: state minOccurs=0
        @type state: State
        '''
        SnapshotBase.__init__(self, instance=instance, snapshotid=snapshotid, current=current, state=state)
