from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceBindingBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[], type=None, serviceid=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'serviceId': {'name': 'serviceid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.properties = properties
        self.type = type
        self.serviceid = serviceid 
