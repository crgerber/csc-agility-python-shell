from core.restclient.v2_0.agilitymodel.base.VersionedItemLink import VersionedItemLinkBase
from core.restclient.v2_0.agilitymodel.actions.VersionedItemLink import VersionedItemLinkActions

class VersionedItemLink(VersionedItemLinkBase, VersionedItemLinkActions):
    '''
    classdocs
    '''
    def __init__(self, slot=None, slotId=None, version=None, latest=None, lockType=None, versionStatus=None):
        '''
        Constructor
        @param slot: slot minOccurs=0
        @type slot: string
        @param slotId: slotId minOccurs=0
        @type slotId: int
        @param version: version minOccurs=0
        @type version: int
        @param latest: latest minOccurs=0
        @type latest: boolean
        @param lockType: lockType minOccurs=0
        @type lockType: int
        @param versionStatus: versionStatus minOccurs=0
        @type versionStatus: string
        '''
        VersionedItemLinkBase.__init__(self, slot=slot, slotId=slotId, version=version, latest=latest, lockType=lockType, versionStatus=versionStatus)
