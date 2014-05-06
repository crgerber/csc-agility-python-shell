from core.agility.v3_0.agilitymodel.base.Domain import DomainBase
from core.agility.v3_0.agilitymodel.actions.Domain import DomainActions

class Domain(DomainBase, DomainActions):
    '''
    classdocs
    '''
    def __init__(self, users=[], roles=[]):
        '''
        Constructor
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: Link
        @param roles: roles minOccurs=0 maxOccurs=unbounded
        @type roles: Link
        '''
        DomainBase.__init__(self, users=users, roles=roles)
