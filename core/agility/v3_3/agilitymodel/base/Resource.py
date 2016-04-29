from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ResourceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, quantity=None, editable=None, hostresource=None, resourcetype=None, subtype=None, units=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'quantity': {'native': True, 'name': 'quantity', 'type': 'float'}, 'editable': {'native': True, 'name': 'editable', 'minOccurs': '0', 'type': 'boolean'}, 'hostResource': {'native': True, 'name': 'hostresource', 'minOccurs': '0', 'type': 'string'}, 'subType': {'native': True, 'name': 'subtype', 'minOccurs': '0', 'type': 'string'}, 'resourceType': {'native': False, 'name': 'resourcetype', 'minOccurs': '0', 'type': 'ResourceType'}, 'units': {'native': True, 'name': 'units', 'minOccurs': '0', 'type': 'string'}})
        self.quantity = quantity
        self.editable = editable
        self.hostresource = hostresource
        self.resourcetype = resourcetype
        self.subtype = subtype
        self.units = units 
