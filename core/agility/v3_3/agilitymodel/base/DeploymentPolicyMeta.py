from core.agility.v3_3.agilitymodel.base.PolicyMeta import PolicyMetaBase

class DeploymentPolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self, designtype=[], resourcetype=[]):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'designType': {'maxOccurs': 'unbounded', 'type': 'AssetTypeBrief', 'name': 'designtype', 'minOccurs': '0', 'native': False}, 'resourceType': {'maxOccurs': 'unbounded', 'type': 'AssetTypeBrief', 'name': 'resourcetype', 'minOccurs': '0', 'native': False}})
        self.designtype = designtype
        self.resourcetype = resourcetype 
