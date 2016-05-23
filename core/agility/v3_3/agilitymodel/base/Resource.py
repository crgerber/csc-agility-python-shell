from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ResourceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, editable=None, quantity=None, units=None, hostresource=None, resourcetype=None, subtype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'editable': {'name': 'editable', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'quantity': {'name': 'quantity', 'native': True, 'type': 'float'}, 'units': {'name': 'units', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'hostResource': {'name': 'hostresource', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'resourceType': {'name': 'resourcetype', 'minOccurs': '0', 'native': False, 'type': 'ResourceType'}, 'subType': {'name': 'subtype', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.editable = editable
        self.quantity = quantity
        self.units = units
        self.hostresource = hostresource
        self.resourcetype = resourcetype
        self.subtype = subtype 
