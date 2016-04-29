from core.agility.v3_3.agilitymodel.base.DeploymentPlan import DeploymentPlanBase
from core.agility.v3_3.agilitymodel.actions.DeploymentPlan import DeploymentPlanActions

class DeploymentPlan(DeploymentPlanBase, DeploymentPlanActions):
    '''
    classdocs
    '''
    def __init__(self, resourceaffinity=None, error=False, resource=[], child=[], option=[], item=None, message='', name='', rank=None, stackdefault=False):
        '''
        Constructor
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param error: error
        @type error: boolean
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: Link
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: DeploymentPlan
        @param option: option minOccurs=0 maxOccurs=unbounded
        @type option: DeploymentPlan
        @param item: item
        @type item: Link
        @param message: message
        @type message: string
        @param name: name
        @type name: string
        @param rank: rank
        @type rank: double
        @param stackdefault: stackdefault
        @type stackdefault: boolean
        '''
        DeploymentPlanBase.__init__(self, resourceaffinity=resourceaffinity, error=error, resource=resource, child=child, option=option, item=item, message=message, name=name, rank=rank, stackdefault=stackdefault)
