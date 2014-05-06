from core.agility.v2_0.agilitymodel.base.SecurityRole import SecurityRoleBase
from core.agility.v2_0.agilitymodel.actions.SecurityRole import SecurityRoleActions

class SecurityRole(SecurityRoleBase, SecurityRoleActions):
    '''
    classdocs
    '''
    def __init__(self, visible=None, product=None, enabled=None, securityRoleName=None):
        '''
        Constructor
        @param visible: visible minOccurs=0
        @type visible: boolean
        @param product: product minOccurs=0
        @type product: Product
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param securityRoleName: securityRoleName minOccurs=0
        @type securityRoleName: string
        '''
        SecurityRoleBase.__init__(self, visible=visible, product=product, enabled=enabled, securityRoleName=securityRoleName)
