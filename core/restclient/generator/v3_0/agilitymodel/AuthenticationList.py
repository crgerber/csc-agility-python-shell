from .base.AuthenticationList import AuthenticationListBase
from .actions.AuthenticationList import AuthenticationListActions

class AuthenticationList(AuthenticationListBase, AuthenticationListActions):
    '''
    classdocs
    '''
    def __init__(self, authentications=[]):
        '''
        Constructor
        @param authentications: authentications minOccurs=0 maxOccurs=unbounded
        @type authentications: Authentication
        '''
        AuthenticationListBase.__init__(self, authentications=authentications)
