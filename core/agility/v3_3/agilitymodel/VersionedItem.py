from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase
from core.agility.v3_3.agilitymodel.actions.VersionedItem import VersionedItemActions

class VersionedItem(VersionedItemBase, VersionedItemActions):
    '''
    classdocs
    '''
    def __init__(self, publishcomment=None, latest=None, versionstatus=None, slotid=None, checkoutallowed=None, slot=None, headallowed=None, version=None, imagepath=None, publisher=None):
        '''
        Constructor
        @param publishcomment: publishcomment minOccurs=0
        @type publishcomment: string
        @param latest: latest minOccurs=0
        @type latest: boolean
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        @param slotid: slotid minOccurs=0
        @type slotid: int
        @param checkoutallowed: checkoutallowed minOccurs=0
        @type checkoutallowed: boolean
        @param slot: slot minOccurs=0
        @type slot: string
        @param headallowed: headallowed minOccurs=0
        @type headallowed: boolean
        @param version: version minOccurs=0
        @type version: int
        @param imagepath: imagepath minOccurs=0
        @type imagepath: string
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        '''
        VersionedItemBase.__init__(self, publishcomment=publishcomment, latest=latest, versionstatus=versionstatus, slotid=slotid, checkoutallowed=checkoutallowed, slot=slot, headallowed=headallowed, version=version, imagepath=imagepath, publisher=publisher)
