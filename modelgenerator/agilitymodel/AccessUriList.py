from base.AccessUriList import AccessUriListBase
from actions.AccessUriList import AccessUriListActions

class AccessUriList(AccessUriListBase, AccessUriListActions):
    '''
    classdocs
    '''
    def __init__(self, AccessUri=list()):
        '''
        Constructor
        @param AccessUri: AccessUri minOccurs=0 maxOccurs=unbounded
        @type AccessUri: AccessUri
        '''
        AccessUriListBase.__init__(self, AccessUri=AccessUri)
