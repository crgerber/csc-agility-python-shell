from core.agility.v3_0.agilitymodel.base.AccessUriList import AccessUriListBase
from core.agility.v3_0.agilitymodel.actions.AccessUriList import AccessUriListActions

class AccessUriList(AccessUriListBase, AccessUriListActions):
    '''
    classdocs
    '''
    def __init__(self, accessuri=[]):
        '''
        Constructor
        @param accessuri: accessuri minOccurs=0 maxOccurs=unbounded
        @type accessuri: AccessUri
        '''
        AccessUriListBase.__init__(self, accessuri=accessuri)
