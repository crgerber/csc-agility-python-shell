from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase
from core.agility.v3_3.agilitymodel.actions.VersionedItem import VersionedItemActions

class VersionedItem(VersionedItemBase, VersionedItemActions):
    '''
    classdocs
    '''
    def __init__(self, slot=None, publisher=None, imagepath=None, headallowed=None, checkoutallowed=None, publishcomment=None, slotid=None, version=None, versionstatus=None, latest=None):
        '''
        Constructor
        @param slot: slot minOccurs=0
        @type slot: string
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param imagepath: imagepath minOccurs=0
        @type imagepath: string
        @param headallowed: headallowed minOccurs=0
        @type headallowed: boolean
        @param checkoutallowed: checkoutallowed minOccurs=0
        @type checkoutallowed: boolean
        @param publishcomment: publishcomment minOccurs=0
        @type publishcomment: string
        @param slotid: slotid minOccurs=0
        @type slotid: int
        @param version: version minOccurs=0
        @type version: int
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        @param latest: latest minOccurs=0
        @type latest: boolean
        '''
        VersionedItemBase.__init__(self, slot=slot, publisher=publisher, imagepath=imagepath, headallowed=headallowed, checkoutallowed=checkoutallowed, publishcomment=publishcomment, slotid=slotid, version=version, versionstatus=versionstatus, latest=latest)
