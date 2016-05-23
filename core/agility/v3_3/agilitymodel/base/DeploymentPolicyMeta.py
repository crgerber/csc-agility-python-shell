from core.agility.v3_3.agilitymodel.base.PolicyMeta import PolicyMetaBase

class DeploymentPolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self, resourcetype=[], designtype=[]):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceType': {'name': 'resourcetype', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetTypeBrief'}, 'designType': {'name': 'designtype', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetTypeBrief'}})
        self.resourcetype = resourcetype
        self.designtype = designtype 
