from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class PolicyAssignmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, itemId=None, itemClass=None, policyTypeName=None, inherited=None, permissioned=None, applyChildrenDepth=None, allowChildrenOverride=False, policy=None, filterMatch=None, itemName=None, applyToSelf=False):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemId': {'type': 'int', 'name': 'itemId', 'minOccurs': '0', 'native': True}, 'itemClass': {'type': 'string', 'name': 'itemClass', 'minOccurs': '0', 'native': True}, 'policyTypeName': {'type': 'string', 'name': 'policyTypeName', 'minOccurs': '0', 'native': True}, 'allowChildrenOverride': {'type': 'boolean', 'name': 'allowChildrenOverride', 'native': True}, 'permissioned': {'type': 'boolean', 'name': 'permissioned', 'minOccurs': '0', 'native': True}, 'applyChildrenDepth': {'type': 'int', 'name': 'applyChildrenDepth', 'minOccurs': '0', 'native': True}, 'inherited': {'type': 'boolean', 'name': 'inherited', 'minOccurs': '0', 'native': True}, 'policy': {'type': 'Link', 'name': 'policy', 'minOccurs': '0', 'native': False}, 'filterMatch': {'type': 'boolean', 'name': 'filterMatch', 'minOccurs': '0', 'native': True}, 'itemName': {'type': 'string', 'name': 'itemName', 'minOccurs': '0', 'native': True}, 'applyToSelf': {'type': 'boolean', 'name': 'applyToSelf', 'native': True}})
        self.itemId = itemId
        self.itemClass = itemClass
        self.policyTypeName = policyTypeName
        self.inherited = inherited
        self.permissioned = permissioned
        self.applyChildrenDepth = applyChildrenDepth
        self.allowChildrenOverride = allowChildrenOverride
        self.policy = policy
        self.filterMatch = filterMatch
        self.itemName = itemName
        self.applyToSelf = applyToSelf 
