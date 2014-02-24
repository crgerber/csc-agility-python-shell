from base.DeploymentPlan import DeploymentPlanBase
from actions.DeploymentPlan import DeploymentPlanActions

class DeploymentPlan(DeploymentPlanBase, DeploymentPlanActions):
    '''
    classdocs
    '''
    def __init__(self, resource=list(), name='', resourceAffinity=None, child=list(), rank=None, item=None, error=False, message='', option=list()):
        '''
        Constructor
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: Link
        @param name: name
        @type name: string
        @param resourceAffinity: resourceAffinity
        @type resourceAffinity: ResourceAffinity
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: DeploymentPlan
        @param rank: rank
        @type rank: double
        @param item: item
        @type item: Link
        @param error: error
        @type error: boolean
        @param message: message
        @type message: string
        @param option: option minOccurs=0 maxOccurs=unbounded
        @type option: DeploymentPlan
        '''
        DeploymentPlanBase.__init__(self, resource=resource, name=name, resourceAffinity=resourceAffinity, child=child, rank=rank, item=item, error=error, message=message, option=option)
