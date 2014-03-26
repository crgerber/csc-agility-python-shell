from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class ResourceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, resourcetype=None, editable=None, subtype=None, hostresource=None, units=None, quantity=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceType': {'type': 'ResourceType', 'name': 'resourcetype', 'minOccurs': '0', 'native': False}, 'editable': {'type': 'boolean', 'name': 'editable', 'minOccurs': '0', 'native': True}, 'subType': {'type': 'string', 'name': 'subtype', 'minOccurs': '0', 'native': True}, 'hostResource': {'type': 'string', 'name': 'hostresource', 'minOccurs': '0', 'native': True}, 'units': {'type': 'string', 'name': 'units', 'minOccurs': '0', 'native': True}, 'quantity': {'type': 'float', 'name': 'quantity', 'native': True}})
        self.resourcetype = resourcetype
        self.editable = editable
        self.subtype = subtype
        self.hostresource = hostresource
        self.units = units
        self.quantity = quantity 
