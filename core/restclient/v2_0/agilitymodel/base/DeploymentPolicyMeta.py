from core.restclient.v2_0.agilitymodel.base.PolicyMeta import PolicyMetaBase

class DeploymentPolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self, designType=list(), resourceType=list()):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'designType': {'maxOccurs': 'unbounded', 'type': 'AssetTypeBrief', 'name': 'designType', 'minOccurs': '0', 'native': False}, 'resourceType': {'maxOccurs': 'unbounded', 'type': 'AssetTypeBrief', 'name': 'resourceType', 'minOccurs': '0', 'native': False}})
        self.designType = designType
        self.resourceType = resourceType 
