from Asset import AssetBase

class ResourceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, resourceType=None, editable=None, subType=None, hostResource=None, units=None, quantity=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceType': {'type': 'ResourceType', 'name': 'resourceType', 'minOccurs': '0', 'native': False}, 'editable': {'type': 'boolean', 'name': 'editable', 'minOccurs': '0', 'native': True}, 'subType': {'type': 'string', 'name': 'subType', 'minOccurs': '0', 'native': True}, 'hostResource': {'type': 'string', 'name': 'hostResource', 'minOccurs': '0', 'native': True}, 'units': {'type': 'string', 'name': 'units', 'minOccurs': '0', 'native': True}, 'quantity': {'type': 'float', 'name': 'quantity', 'native': True}})
        self.resourceType = resourceType
        self.editable = editable
        self.subType = subType
        self.hostResource = hostResource
        self.units = units
        self.quantity = quantity 
