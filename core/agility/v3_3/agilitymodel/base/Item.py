from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ItemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, lastmodified=None, locktype=None, domain=None, policyassignment=[], parent=None, created=None, creator=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'lastModified': {'native': True, 'name': 'lastmodified', 'minOccurs': '0', 'type': 'date'}, 'lockType': {'native': True, 'name': 'locktype', 'minOccurs': '0', 'type': 'int'}, 'domain': {'native': False, 'name': 'domain', 'minOccurs': '0', 'type': 'Link'}, 'policyAssignment': {'maxOccurs': 'unbounded', 'native': False, 'name': 'policyassignment', 'minOccurs': '0', 'type': 'PolicyAssignment'}, 'parent': {'native': False, 'name': 'parent', 'minOccurs': '0', 'type': 'Link'}, 'creator': {'native': False, 'name': 'creator', 'minOccurs': '0', 'type': 'Link'}, 'created': {'native': True, 'name': 'created', 'minOccurs': '0', 'type': 'date'}})
        self.lastmodified = lastmodified
        self.locktype = locktype
        self.domain = domain
        self.policyassignment = policyassignment
        self.parent = parent
        self.created = created
        self.creator = creator 
