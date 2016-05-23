from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PolicyAssignmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, permissioned=None, allowchildrenoverride=False, inherited=None, itemname=None, itemclass=None, applychildrendepth=None, policy=None, itemid=None, applytoself=False, policytypename=None, filtermatch=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'permissioned': {'name': 'permissioned', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'allowChildrenOverride': {'name': 'allowchildrenoverride', 'native': True, 'type': 'boolean'}, 'policyTypeName': {'name': 'policytypename', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'itemName': {'name': 'itemname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'itemClass': {'name': 'itemclass', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'policy': {'name': 'policy', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'itemId': {'name': 'itemid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'applyChildrenDepth': {'name': 'applychildrendepth', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'applyToSelf': {'name': 'applytoself', 'native': True, 'type': 'boolean'}, 'inherited': {'name': 'inherited', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'filterMatch': {'name': 'filtermatch', 'minOccurs': '0', 'native': True, 'type': 'boolean'}})
        self.permissioned = permissioned
        self.allowchildrenoverride = allowchildrenoverride
        self.inherited = inherited
        self.itemname = itemname
        self.itemclass = itemclass
        self.applychildrendepth = applychildrendepth
        self.policy = policy
        self.itemid = itemid
        self.applytoself = applytoself
        self.policytypename = policytypename
        self.filtermatch = filtermatch 
