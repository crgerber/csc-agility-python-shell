from core.agility.v3_0.agilitymodel.base.AuthenticationList import AuthenticationListBase
from core.agility.v3_0.agilitymodel.actions.AuthenticationList import AuthenticationListActions

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
