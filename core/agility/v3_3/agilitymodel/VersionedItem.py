from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase
from core.agility.v3_3.agilitymodel.actions.VersionedItem import VersionedItemActions

class VersionedItem(VersionedItemBase, VersionedItemActions):
    '''
    classdocs
    '''
    def __init__(self, slotid=None, slot=None, versionstatus=None, publisher=None, latest=None, version=None, headallowed=None, imagepath=None, checkoutallowed=None, publishcomment=None):
        '''
        Constructor
        @param slotid: slotid minOccurs=0
        @type slotid: int
        @param slot: slot minOccurs=0
        @type slot: string
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param latest: latest minOccurs=0
        @type latest: boolean
        @param version: version minOccurs=0
        @type version: int
        @param headallowed: headallowed minOccurs=0
        @type headallowed: boolean
        @param imagepath: imagepath minOccurs=0
        @type imagepath: string
        @param checkoutallowed: checkoutallowed minOccurs=0
        @type checkoutallowed: boolean
        @param publishcomment: publishcomment minOccurs=0
        @type publishcomment: string
        '''
        VersionedItemBase.__init__(self, slotid=slotid, slot=slot, versionstatus=versionstatus, publisher=publisher, latest=latest, version=version, headallowed=headallowed, imagepath=imagepath, checkoutallowed=checkoutallowed, publishcomment=publishcomment)
