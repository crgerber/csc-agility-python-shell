from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class ServiceBindingBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, serviceId=None, type=None, properties=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceId': {'type': 'string', 'name': 'serviceId', 'minOccurs': '0', 'native': True}, 'type': {'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.serviceId = serviceId
        self.type = type
        self.properties = properties 
