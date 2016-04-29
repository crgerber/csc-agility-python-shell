from core.agility.v3_3.agilitymodel.base.Domain import DomainBase
from core.agility.v3_3.agilitymodel.actions.Domain import DomainActions

class Domain(DomainBase, DomainActions):
    '''
    classdocs
    '''
    def __init__(self, roles=[], users=[]):
        '''
        Constructor
        @param roles: roles minOccurs=0 maxOccurs=unbounded
        @type roles: Link
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: Link
        '''
        DomainBase.__init__(self, roles=roles, users=users)
