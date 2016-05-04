from core.agility.v3_3.agilitymodel.base.Project import ProjectBase
from core.agility.v3_3.agilitymodel.actions.Project import ProjectActions

class Project(ProjectBase, ProjectActions):
    '''
    classdocs
    '''
    def __init__(self, solution=[], environments=[], sourceprojecttemplate=None):
        '''
        Constructor
        @param solution: solution minOccurs=0 maxOccurs=unbounded
        @type solution: Link
        @param environments: environments minOccurs=0 maxOccurs=unbounded
        @type environments: Link
        @param sourceprojecttemplate: sourceprojecttemplate minOccurs=0
        @type sourceprojecttemplate: Link
        '''
        ProjectBase.__init__(self, solution=solution, environments=environments, sourceprojecttemplate=sourceprojecttemplate)
