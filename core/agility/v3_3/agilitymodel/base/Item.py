from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ItemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, created=None, creator=None, lastmodified=None, locktype=None, domain=None, parent=None, policyassignment=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'created': {'name': 'created', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'creator': {'name': 'creator', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'lastModified': {'name': 'lastmodified', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'lockType': {'name': 'locktype', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'domain': {'name': 'domain', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'parent': {'name': 'parent', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'policyAssignment': {'name': 'policyassignment', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PolicyAssignment'}})
        self.created = created
        self.creator = creator
        self.lastmodified = lastmodified
        self.locktype = locktype
        self.domain = domain
        self.parent = parent
        self.policyassignment = policyassignment 
