from core.agility.v3_3.agilitymodel.base.SecurityRole import SecurityRoleBase
from core.agility.v3_3.agilitymodel.actions.SecurityRole import SecurityRoleActions

class SecurityRole(SecurityRoleBase, SecurityRoleActions):
    '''
    classdocs
    '''
    def __init__(self, product=None, enabled=None, visible=None, securityrolename=None):
        '''
        Constructor
        @param product: product minOccurs=0
        @type product: Product
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param visible: visible minOccurs=0
        @type visible: boolean
        @param securityrolename: securityrolename minOccurs=0
        @type securityrolename: string
        '''
        SecurityRoleBase.__init__(self, product=product, enabled=enabled, visible=visible, securityrolename=securityrolename)
