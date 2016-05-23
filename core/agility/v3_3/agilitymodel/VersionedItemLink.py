from core.agility.v3_3.agilitymodel.base.VersionedItemLink import VersionedItemLinkBase
from core.agility.v3_3.agilitymodel.actions.VersionedItemLink import VersionedItemLinkActions

class VersionedItemLink(VersionedItemLinkBase, VersionedItemLinkActions):
    '''
    classdocs
    '''
    def __init__(self, slotid=None, slot=None, versionstatus=None, latest=None, version=None, locktype=None):
        '''
        Constructor
        @param slotid: slotid minOccurs=0
        @type slotid: int
        @param slot: slot minOccurs=0
        @type slot: string
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        @param latest: latest minOccurs=0
        @type latest: boolean
        @param version: version minOccurs=0
        @type version: int
        @param locktype: locktype minOccurs=0
        @type locktype: int
        '''
        VersionedItemLinkBase.__init__(self, slotid=slotid, slot=slot, versionstatus=versionstatus, latest=latest, version=version, locktype=locktype)
