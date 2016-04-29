from .base.Project import ProjectBase
from .actions.Project import ProjectActions

class Project(ProjectBase, ProjectActions):
    '''
    classdocs
    '''
    def __init__(self, solution=[], environments=[]):
        '''
        Constructor
        @param solution: solution minOccurs=0 maxOccurs=unbounded
        @type solution: Link
        @param environments: environments minOccurs=0 maxOccurs=unbounded
        @type environments: Link
        '''
        ProjectBase.__init__(self, solution=solution, environments=environments)
