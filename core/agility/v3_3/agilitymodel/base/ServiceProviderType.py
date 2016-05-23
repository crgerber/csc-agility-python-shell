from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceProviderTypeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, sdkservice=False, supertype=[], servicetypesupertype=[], option=[], adapter=None, servicetype=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'sdkService': {'name': 'sdkservice', 'native': True, 'type': 'boolean'}, 'serviceTypeSuperType': {'name': 'servicetypesupertype', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'superType': {'name': 'supertype', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'adapter': {'name': 'adapter', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'option': {'name': 'option', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ServiceProviderOption'}, 'serviceType': {'name': 'servicetype', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.sdkservice = sdkservice
        self.supertype = supertype
        self.servicetypesupertype = servicetypesupertype
        self.option = option
        self.adapter = adapter
        self.servicetype = servicetype 
