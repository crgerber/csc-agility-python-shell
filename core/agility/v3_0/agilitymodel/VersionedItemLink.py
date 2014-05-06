from core.agility.v3_0.agilitymodel.base.VersionedItemLink import VersionedItemLinkBase
from core.agility.v3_0.agilitymodel.actions.VersionedItemLink import VersionedItemLinkActions

class VersionedItemLink(VersionedItemLinkBase, VersionedItemLinkActions):
    '''
    classdocs
    '''
    def __init__(self, slot=None, slotid=None, version=None, latest=None, locktype=None, versionstatus=None):
        '''
        Constructor
        @param slot: slot minOccurs=0
        @type slot: string
        @param slotid: slotid minOccurs=0
        @type slotid: int
        @param version: version minOccurs=0
        @type version: int
        @param latest: latest minOccurs=0
        @type latest: boolean
        @param locktype: locktype minOccurs=0
        @type locktype: int
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        '''
        VersionedItemLinkBase.__init__(self, slot=slot, slotid=slotid, version=version, latest=latest, locktype=locktype, versionstatus=versionstatus)
