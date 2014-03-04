from core.restclient.v2_0.agilitymodel.base.VersionedItem import VersionedItemBase
from core.restclient.v2_0.agilitymodel.actions.VersionedItem import VersionedItemActions

class VersionedItem(VersionedItemBase, VersionedItemActions):
    '''
    classdocs
    '''
    def __init__(self, slot=None, publisher=None, imagePath=None, checkoutAllowed=False, publishComment=None, slotId=None, version=None, status=None, versionStatus=None, latest=None):
        '''
        Constructor
        @param slot: slot minOccurs=0
        @type slot: string
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param imagePath: imagePath minOccurs=0
        @type imagePath: string
        @param checkoutAllowed: checkoutAllowed
        @type checkoutAllowed: boolean
        @param publishComment: publishComment minOccurs=0
        @type publishComment: string
        @param slotId: slotId minOccurs=0
        @type slotId: int
        @param version: version minOccurs=0
        @type version: int
        @param status: status minOccurs=0
        @type status: string
        @param versionStatus: versionStatus minOccurs=0
        @type versionStatus: string
        @param latest: latest minOccurs=0
        @type latest: boolean
        '''
        VersionedItemBase.__init__(self, slot=slot, publisher=publisher, imagePath=imagePath, checkoutAllowed=checkoutAllowed, publishComment=publishComment, slotId=slotId, version=version, status=status, versionStatus=versionStatus, latest=latest)
