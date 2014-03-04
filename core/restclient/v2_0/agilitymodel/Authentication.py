from core.restclient.v2_0.agilitymodel.base.Authentication import AuthenticationBase
from core.restclient.v2_0.agilitymodel.actions.Authentication import AuthenticationActions

class Authentication(AuthenticationBase, AuthenticationActions):
    '''
    classdocs
    '''
    def __init__(self, type=None, properties=list()):
        '''
        Constructor
        @param type: type
        @type type: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        AuthenticationBase.__init__(self, type=type, properties=properties)
