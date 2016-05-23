from core.agility.v3_3.agilitymodel.base.Authentication import AuthenticationBase
from core.agility.v3_3.agilitymodel.actions.Authentication import AuthenticationActions

class Authentication(AuthenticationBase, AuthenticationActions):
    '''
    classdocs
    '''
    def __init__(self, orderposition=None, authgroups=[], properties=[], type=None, disabled=False):
        '''
        Constructor
        @param orderposition: orderposition minOccurs=0
        @type orderposition: int
        @param authgroups: authgroups minOccurs=0 maxOccurs=unbounded
        @type authgroups: AuthGroup
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param type: type
        @type type: Link
        @param disabled: disabled
        @type disabled: boolean
        '''
        AuthenticationBase.__init__(self, orderposition=orderposition, authgroups=authgroups, properties=properties, type=type, disabled=disabled)
