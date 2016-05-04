from base.PlannerApplication import PlannerApplicationBase
from actions.PlannerApplication import PlannerApplicationActions

class PlannerApplication(PlannerApplicationBase, PlannerApplicationActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        PlannerApplicationBase.__init__(self)
