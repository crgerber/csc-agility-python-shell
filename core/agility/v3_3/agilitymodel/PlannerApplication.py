from core.agility.v3_3.agilitymodel.base.PlannerApplication import PlannerApplicationBase
from core.agility.v3_3.agilitymodel.actions.PlannerApplication import PlannerApplicationActions

class PlannerApplication(PlannerApplicationBase, PlannerApplicationActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        PlannerApplicationBase.__init__(self)
