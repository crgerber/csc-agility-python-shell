from .base.VersionedItem import VersionedItemBase
from .actions.VersionedItem import VersionedItemActions

class VersionedItem(VersionedItemBase, VersionedItemActions):
    '''
    classdocs
    '''
    def __init__(self, slot=None, publisher=None, imagepath=None, checkoutallowed=False, publishcomment=None, slotid=None, version=None, status=None, versionstatus=None, latest=None):
        '''
        Constructor
        @param slot: slot minOccurs=0
        @type slot: string
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param imagepath: imagepath minOccurs=0
        @type imagepath: string
        @param checkoutallowed: checkoutallowed
        @type checkoutallowed: boolean
        @param publishcomment: publishcomment minOccurs=0
        @type publishcomment: string
        @param slotid: slotid minOccurs=0
        @type slotid: int
        @param version: version minOccurs=0
        @type version: int
        @param status: status minOccurs=0
        @type status: string
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        @param latest: latest minOccurs=0
        @type latest: boolean
        '''
        VersionedItemBase.__init__(self, slot=slot, publisher=publisher, imagepath=imagepath, checkoutallowed=checkoutallowed, publishcomment=publishcomment, slotid=slotid, version=version, status=status, versionstatus=versionstatus, latest=latest)
