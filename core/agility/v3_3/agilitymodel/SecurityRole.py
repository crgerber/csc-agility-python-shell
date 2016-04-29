from core.agility.v3_3.agilitymodel.base.SecurityRole import SecurityRoleBase
from core.agility.v3_3.agilitymodel.actions.SecurityRole import SecurityRoleActions

class SecurityRole(SecurityRoleBase, SecurityRoleActions):
    '''
    classdocs
    '''
    def __init__(self, enabled=None, securityrolename=None, product=None, visible=None):
        '''
        Constructor
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param securityrolename: securityrolename minOccurs=0
        @type securityrolename: string
        @param product: product minOccurs=0
        @type product: Product
        @param visible: visible minOccurs=0
        @type visible: boolean
        '''
        SecurityRoleBase.__init__(self, enabled=enabled, securityrolename=securityrolename, product=product, visible=visible)
