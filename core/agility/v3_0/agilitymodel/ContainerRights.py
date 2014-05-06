from core.agility.v3_0.agilitymodel.base.ContainerRights import ContainerRightsBase
from core.agility.v3_0.agilitymodel.actions.ContainerRights import ContainerRightsActions

class ContainerRights(ContainerRightsBase, ContainerRightsActions):
    '''
    classdocs
    '''
    def __init__(self, projectrole=None, rights=[], user=[], usergroup=[]):
        '''
        Constructor
        @param projectrole: projectrole minOccurs=0
        @type projectrole: Link
        @param rights: rights minOccurs=0 maxOccurs=unbounded
        @type rights: AccessRightSet
        @param user: user minOccurs=0 maxOccurs=unbounded
        @type user: Link
        @param usergroup: usergroup minOccurs=0 maxOccurs=unbounded
        @type usergroup: Link
        '''
        ContainerRightsBase.__init__(self, projectrole=projectrole, rights=rights, user=user, usergroup=usergroup)
