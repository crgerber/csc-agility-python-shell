from base.ContainerRights import ContainerRightsBase
from actions.ContainerRights import ContainerRightsActions

class ContainerRights(ContainerRightsBase, ContainerRightsActions):
    '''
    classdocs
    '''
    def __init__(self, projectRole=None, rights=list(), user=list(), usergroup=list()):
        '''
        Constructor
        @param projectRole: projectRole minOccurs=0
        @type projectRole: Link
        @param rights: rights minOccurs=0 maxOccurs=unbounded
        @type rights: AccessRightSet
        @param user: user minOccurs=0 maxOccurs=unbounded
        @type user: Link
        @param usergroup: usergroup minOccurs=0 maxOccurs=unbounded
        @type usergroup: Link
        '''
        ContainerRightsBase.__init__(self, projectRole=projectRole, rights=rights, user=user, usergroup=usergroup)
