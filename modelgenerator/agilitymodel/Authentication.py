from base.Authentication import AuthenticationBase
from actions.Authentication import AuthenticationActions

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
