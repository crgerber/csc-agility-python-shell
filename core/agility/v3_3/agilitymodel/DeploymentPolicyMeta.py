from core.agility.v3_3.agilitymodel.base.DeploymentPolicyMeta import DeploymentPolicyMetaBase
from core.agility.v3_3.agilitymodel.actions.DeploymentPolicyMeta import DeploymentPolicyMetaActions

class DeploymentPolicyMeta(DeploymentPolicyMetaBase, DeploymentPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, resourcetype=[], designtype=[]):
        '''
        Constructor
        @param resourcetype: resourcetype minOccurs=0 maxOccurs=unbounded
        @type resourcetype: AssetTypeBrief
        @param designtype: designtype minOccurs=0 maxOccurs=unbounded
        @type designtype: AssetTypeBrief
        '''
        DeploymentPolicyMetaBase.__init__(self, resourcetype=resourcetype, designtype=designtype)
