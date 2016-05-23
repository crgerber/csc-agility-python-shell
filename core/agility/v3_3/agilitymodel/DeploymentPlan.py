from core.agility.v3_3.agilitymodel.base.DeploymentPlan import DeploymentPlanBase
from core.agility.v3_3.agilitymodel.actions.DeploymentPlan import DeploymentPlanActions

class DeploymentPlan(DeploymentPlanBase, DeploymentPlanActions):
    '''
    classdocs
    '''
    def __init__(self, message='', rank=None, stackdefault=False, option=[], name='', resourceaffinity=None, resource=[], child=[], error=False, item=None):
        '''
        Constructor
        @param message: message
        @type message: string
        @param rank: rank
        @type rank: double
        @param stackdefault: stackdefault
        @type stackdefault: boolean
        @param option: option minOccurs=0 maxOccurs=unbounded
        @type option: DeploymentPlan
        @param name: name
        @type name: string
        @param resourceaffinity: resourceaffinity
        @type resourceaffinity: ResourceAffinity
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: Link
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: DeploymentPlan
        @param error: error
        @type error: boolean
        @param item: item
        @type item: Link
        '''
        DeploymentPlanBase.__init__(self, message=message, rank=rank, stackdefault=stackdefault, option=option, name=name, resourceaffinity=resourceaffinity, resource=resource, child=child, error=error, item=item)
