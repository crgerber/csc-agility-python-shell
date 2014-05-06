from core.agility.v2_0.agilitymodel.base.ProjectRole import ProjectRoleBase
from core.agility.v2_0.agilitymodel.actions.ProjectRole import ProjectRoleActions

class ProjectRole(ProjectRoleBase, ProjectRoleActions):
    '''
    classdocs
    '''
    def __init__(self, domain=None):
        '''
        Constructor
        @param domain: domain minOccurs=0
        @type domain: Link
        '''
        ProjectRoleBase.__init__(self, domain=domain)
