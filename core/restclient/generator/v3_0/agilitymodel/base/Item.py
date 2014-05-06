from Asset import AssetBase

class ItemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, domain=None, parent=None, created=None, lastmodified=None, creator=None, policyassignment=[], locktype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'domain': {'type': 'Link', 'name': 'domain', 'minOccurs': '0', 'native': False}, 'parent': {'type': 'Link', 'name': 'parent', 'minOccurs': '0', 'native': False}, 'creator': {'type': 'Link', 'name': 'creator', 'minOccurs': '0', 'native': False}, 'lastModified': {'type': 'date', 'name': 'lastmodified', 'minOccurs': '0', 'native': True}, 'created': {'type': 'date', 'name': 'created', 'minOccurs': '0', 'native': True}, 'policyAssignment': {'maxOccurs': 'unbounded', 'type': 'PolicyAssignment', 'name': 'policyassignment', 'minOccurs': '0', 'native': False}, 'lockType': {'type': 'int', 'name': 'locktype', 'minOccurs': '0', 'native': True}})
        self.domain = domain
        self.parent = parent
        self.created = created
        self.lastmodified = lastmodified
        self.creator = creator
        self.policyassignment = policyassignment
        self.locktype = locktype 
