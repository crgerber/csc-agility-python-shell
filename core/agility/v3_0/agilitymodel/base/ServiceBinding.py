from core.agility.v3_0.agilitymodel.base.Item import ItemBase

class ServiceBindingBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, serviceid=None, type=None, properties=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceId': {'type': 'string', 'name': 'serviceid', 'minOccurs': '0', 'native': True}, 'type': {'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.serviceid = serviceid
        self.type = type
        self.properties = properties 
