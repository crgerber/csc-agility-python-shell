from Item import ItemBase

class ServiceProviderTypeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, servicetype=[], option=[], adapter=None, servicetypesupertype=[], sdkservice=False, supertype=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceType': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'servicetype', 'minOccurs': '0', 'native': False}, 'option': {'maxOccurs': 'unbounded', 'type': 'ServiceProviderOption', 'name': 'option', 'minOccurs': '0', 'native': False}, 'adapter': {'type': 'string', 'name': 'adapter', 'minOccurs': '0', 'native': True}, 'serviceTypeSuperType': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'servicetypesupertype', 'minOccurs': '0', 'native': False}, 'sdkService': {'type': 'boolean', 'name': 'sdkservice', 'native': True}, 'superType': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'supertype', 'minOccurs': '0', 'native': False}})
        self.servicetype = servicetype
        self.option = option
        self.adapter = adapter
        self.servicetypesupertype = servicetypesupertype
        self.sdkservice = sdkservice
        self.supertype = supertype 
