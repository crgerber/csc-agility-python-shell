from core.agility.v3_3.agilitymodel.base.ProjectRole import ProjectRoleBase
from core.agility.v3_3.agilitymodel.actions.ProjectRole import ProjectRoleActions

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
