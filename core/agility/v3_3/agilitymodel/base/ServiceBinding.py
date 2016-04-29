from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceBindingBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, type=None, serviceid=None, properties=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'serviceId': {'native': True, 'name': 'serviceid', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'Link'}})
        self.type = type
        self.serviceid = serviceid
        self.properties = properties 
