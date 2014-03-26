from Asset import AssetBase

class PolicyAssignmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, itemid=None, itemclass=None, policytypename=None, inherited=None, permissioned=None, applychildrendepth=None, allowchildrenoverride=False, policy=None, filtermatch=None, itemname=None, applytoself=False):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemId': {'type': 'int', 'name': 'itemid', 'minOccurs': '0', 'native': True}, 'itemClass': {'type': 'string', 'name': 'itemclass', 'minOccurs': '0', 'native': True}, 'policyTypeName': {'type': 'string', 'name': 'policytypename', 'minOccurs': '0', 'native': True}, 'allowChildrenOverride': {'type': 'boolean', 'name': 'allowchildrenoverride', 'native': True}, 'permissioned': {'type': 'boolean', 'name': 'permissioned', 'minOccurs': '0', 'native': True}, 'applyChildrenDepth': {'type': 'int', 'name': 'applychildrendepth', 'minOccurs': '0', 'native': True}, 'inherited': {'type': 'boolean', 'name': 'inherited', 'minOccurs': '0', 'native': True}, 'policy': {'type': 'Link', 'name': 'policy', 'minOccurs': '0', 'native': False}, 'filterMatch': {'type': 'boolean', 'name': 'filtermatch', 'minOccurs': '0', 'native': True}, 'itemName': {'type': 'string', 'name': 'itemname', 'minOccurs': '0', 'native': True}, 'applyToSelf': {'type': 'boolean', 'name': 'applytoself', 'native': True}})
        self.itemid = itemid
        self.itemclass = itemclass
        self.policytypename = policytypename
        self.inherited = inherited
        self.permissioned = permissioned
        self.applychildrendepth = applychildrendepth
        self.allowchildrenoverride = allowchildrenoverride
        self.policy = policy
        self.filtermatch = filtermatch
        self.itemname = itemname
        self.applytoself = applytoself 
