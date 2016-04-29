from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PolicyAssignmentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, inherited=None, itemname=None, applytoself=False, filtermatch=None, allowchildrenoverride=False, applychildrendepth=None, policytypename=None, itemid=None, itemclass=None, permissioned=None, policy=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'inherited': {'native': True, 'name': 'inherited', 'minOccurs': '0', 'type': 'boolean'}, 'policyTypeName': {'native': True, 'name': 'policytypename', 'minOccurs': '0', 'type': 'string'}, 'applyToSelf': {'native': True, 'name': 'applytoself', 'type': 'boolean'}, 'policy': {'native': False, 'name': 'policy', 'minOccurs': '0', 'type': 'Link'}, 'allowChildrenOverride': {'native': True, 'name': 'allowchildrenoverride', 'type': 'boolean'}, 'applyChildrenDepth': {'native': True, 'name': 'applychildrendepth', 'minOccurs': '0', 'type': 'int'}, 'itemName': {'native': True, 'name': 'itemname', 'minOccurs': '0', 'type': 'string'}, 'itemId': {'native': True, 'name': 'itemid', 'minOccurs': '0', 'type': 'int'}, 'itemClass': {'native': True, 'name': 'itemclass', 'minOccurs': '0', 'type': 'string'}, 'permissioned': {'native': True, 'name': 'permissioned', 'minOccurs': '0', 'type': 'boolean'}, 'filterMatch': {'native': True, 'name': 'filtermatch', 'minOccurs': '0', 'type': 'boolean'}})
        self.inherited = inherited
        self.itemname = itemname
        self.applytoself = applytoself
        self.filtermatch = filtermatch
        self.allowchildrenoverride = allowchildrenoverride
        self.applychildrendepth = applychildrendepth
        self.policytypename = policytypename
        self.itemid = itemid
        self.itemclass = itemclass
        self.permissioned = permissioned
        self.policy = policy 
