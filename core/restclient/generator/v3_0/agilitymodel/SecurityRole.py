from .base.SecurityRole import SecurityRoleBase
from .actions.SecurityRole import SecurityRoleActions

class SecurityRole(SecurityRoleBase, SecurityRoleActions):
    '''
    classdocs
    '''
    def __init__(self, visible=None, product=None, enabled=None, securityrolename=None):
        '''
        Constructor
        @param visible: visible minOccurs=0
        @type visible: boolean
        @param product: product minOccurs=0
        @type product: Product
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param securityrolename: securityrolename minOccurs=0
        @type securityrolename: string
        '''
        SecurityRoleBase.__init__(self, visible=visible, product=product, enabled=enabled, securityrolename=securityrolename)
