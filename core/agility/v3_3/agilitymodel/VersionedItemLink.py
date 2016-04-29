from core.agility.v3_3.agilitymodel.base.VersionedItemLink import VersionedItemLinkBase
from core.agility.v3_3.agilitymodel.actions.VersionedItemLink import VersionedItemLinkActions

class VersionedItemLink(VersionedItemLinkBase, VersionedItemLinkActions):
    '''
    classdocs
    '''
    def __init__(self, latest=None, versionstatus=None, locktype=None, slotid=None, slot=None, version=None):
        '''
        Constructor
        @param latest: latest minOccurs=0
        @type latest: boolean
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        @param locktype: locktype minOccurs=0
        @type locktype: int
        @param slotid: slotid minOccurs=0
        @type slotid: int
        @param slot: slot minOccurs=0
        @type slot: string
        @param version: version minOccurs=0
        @type version: int
        '''
        VersionedItemLinkBase.__init__(self, latest=latest, versionstatus=versionstatus, locktype=locktype, slotid=slotid, slot=slot, version=version)
