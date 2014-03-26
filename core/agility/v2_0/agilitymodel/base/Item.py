from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class ItemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, domain=None, parent=None, created=None, lastModified=None, creator=None, policyAssignment=list(), lockType=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'domain': {'type': 'Link', 'name': 'domain', 'minOccurs': '0', 'native': False}, 'parent': {'type': 'Link', 'name': 'parent', 'minOccurs': '0', 'native': False}, 'creator': {'type': 'Link', 'name': 'creator', 'minOccurs': '0', 'native': False}, 'lastModified': {'type': 'date', 'name': 'lastModified', 'minOccurs': '0', 'native': True}, 'created': {'type': 'date', 'name': 'created', 'minOccurs': '0', 'native': True}, 'policyAssignment': {'maxOccurs': 'unbounded', 'type': 'PolicyAssignment', 'name': 'policyAssignment', 'minOccurs': '0', 'native': False}, 'lockType': {'type': 'int', 'name': 'lockType', 'minOccurs': '0', 'native': True}})
        self.domain = domain
        self.parent = parent
        self.created = created
        self.lastModified = lastModified
        self.creator = creator
        self.policyAssignment = policyAssignment
        self.lockType = lockType 
