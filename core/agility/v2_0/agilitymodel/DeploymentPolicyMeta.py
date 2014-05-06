from core.agility.v2_0.agilitymodel.base.DeploymentPolicyMeta import DeploymentPolicyMetaBase
from core.agility.v2_0.agilitymodel.actions.DeploymentPolicyMeta import DeploymentPolicyMetaActions

class DeploymentPolicyMeta(DeploymentPolicyMetaBase, DeploymentPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, designType=list(), resourceType=list()):
        '''
        Constructor
        @param designType: designType minOccurs=0 maxOccurs=unbounded
        @type designType: AssetTypeBrief
        @param resourceType: resourceType minOccurs=0 maxOccurs=unbounded
        @type resourceType: AssetTypeBrief
        '''
        DeploymentPolicyMetaBase.__init__(self, designType=designType, resourceType=resourceType)
