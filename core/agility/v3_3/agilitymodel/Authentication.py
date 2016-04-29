from core.agility.v3_3.agilitymodel.base.Authentication import AuthenticationBase
from core.agility.v3_3.agilitymodel.actions.Authentication import AuthenticationActions

class Authentication(AuthenticationBase, AuthenticationActions):
    '''
    classdocs
    '''
    def __init__(self, orderposition=None, properties=[], disabled=False, authgroups=[], type=None):
        '''
        Constructor
        @param orderposition: orderposition minOccurs=0
        @type orderposition: int
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param disabled: disabled
        @type disabled: boolean
        @param authgroups: authgroups minOccurs=0 maxOccurs=unbounded
        @type authgroups: AuthGroup
        @param type: type
        @type type: Link
        '''
        AuthenticationBase.__init__(self, orderposition=orderposition, properties=properties, disabled=disabled, authgroups=authgroups, type=type)
