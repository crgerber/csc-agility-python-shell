from core.agility.v3_3.agilitymodel.base.AuthenticationType import AuthenticationTypeBase
from core.agility.v3_3.agilitymodel.actions.AuthenticationType import AuthenticationTypeActions

class AuthenticationType(AuthenticationTypeBase, AuthenticationTypeActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], type=''):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param type: type
        @type type: string
        '''
        AuthenticationTypeBase.__init__(self, properties=properties, type=type)
