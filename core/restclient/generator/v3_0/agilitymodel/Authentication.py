from base.Authentication import AuthenticationBase
from actions.Authentication import AuthenticationActions

class Authentication(AuthenticationBase, AuthenticationActions):
    '''
    classdocs
    '''
    def __init__(self, disabled=False, orderposition=None, type=None, properties=[], authgroups=[]):
        '''
        Constructor
        @param disabled: disabled
        @type disabled: boolean
        @param orderposition: orderposition minOccurs=0
        @type orderposition: int
        @param type: type
        @type type: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param authgroups: authgroups minOccurs=0 maxOccurs=unbounded
        @type authgroups: AuthGroup
        '''
        AuthenticationBase.__init__(self, disabled=disabled, orderposition=orderposition, type=type, properties=properties, authgroups=authgroups)
