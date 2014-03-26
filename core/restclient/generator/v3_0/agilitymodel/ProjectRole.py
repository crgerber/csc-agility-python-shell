from base.ProjectRole import ProjectRoleBase
from actions.ProjectRole import ProjectRoleActions

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
