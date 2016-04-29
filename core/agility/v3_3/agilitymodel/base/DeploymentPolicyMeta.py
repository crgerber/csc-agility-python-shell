from core.agility.v3_3.agilitymodel.base.PolicyMeta import PolicyMetaBase

class DeploymentPolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self, resourcetype=[], designtype=[]):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceType': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resourcetype', 'minOccurs': '0', 'type': 'AssetTypeBrief'}, 'designType': {'maxOccurs': 'unbounded', 'native': False, 'name': 'designtype', 'minOccurs': '0', 'type': 'AssetTypeBrief'}})
        self.resourcetype = resourcetype
        self.designtype = designtype 
