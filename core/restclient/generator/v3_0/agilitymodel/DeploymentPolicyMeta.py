from .base.DeploymentPolicyMeta import DeploymentPolicyMetaBase
from .actions.DeploymentPolicyMeta import DeploymentPolicyMetaActions

class DeploymentPolicyMeta(DeploymentPolicyMetaBase, DeploymentPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, designtype=[], resourcetype=[]):
        '''
        Constructor
        @param designtype: designtype minOccurs=0 maxOccurs=unbounded
        @type designtype: AssetTypeBrief
        @param resourcetype: resourcetype minOccurs=0 maxOccurs=unbounded
        @type resourcetype: AssetTypeBrief
        '''
        DeploymentPolicyMetaBase.__init__(self, designtype=designtype, resourcetype=resourcetype)
