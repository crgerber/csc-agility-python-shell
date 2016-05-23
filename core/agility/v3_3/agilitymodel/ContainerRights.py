from core.agility.v3_3.agilitymodel.base.ContainerRights import ContainerRightsBase
from core.agility.v3_3.agilitymodel.actions.ContainerRights import ContainerRightsActions

class ContainerRights(ContainerRightsBase, ContainerRightsActions):
    '''
    classdocs
    '''
    def __init__(self, rights=[], projectrole=None, usergroup=[], user=[]):
        '''
        Constructor
        @param rights: rights minOccurs=0 maxOccurs=unbounded
        @type rights: AccessRightSet
        @param projectrole: projectrole minOccurs=0
        @type projectrole: Link
        @param usergroup: usergroup minOccurs=0 maxOccurs=unbounded
        @type usergroup: Link
        @param user: user minOccurs=0 maxOccurs=unbounded
        @type user: Link
        '''
        ContainerRightsBase.__init__(self, rights=rights, projectrole=projectrole, usergroup=usergroup, user=user)
