from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceProviderTypeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, servicetypesupertype=[], sdkservice=False, servicetype=[], option=[], adapter=None, supertype=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceTypeSuperType': {'maxOccurs': 'unbounded', 'native': False, 'name': 'servicetypesupertype', 'minOccurs': '0', 'type': 'Link'}, 'sdkService': {'native': True, 'name': 'sdkservice', 'type': 'boolean'}, 'superType': {'maxOccurs': 'unbounded', 'native': False, 'name': 'supertype', 'minOccurs': '0', 'type': 'Link'}, 'option': {'maxOccurs': 'unbounded', 'native': False, 'name': 'option', 'minOccurs': '0', 'type': 'ServiceProviderOption'}, 'adapter': {'native': True, 'name': 'adapter', 'minOccurs': '0', 'type': 'string'}, 'serviceType': {'maxOccurs': 'unbounded', 'native': False, 'name': 'servicetype', 'minOccurs': '0', 'type': 'Link'}})
        self.servicetypesupertype = servicetypesupertype
        self.sdkservice = sdkservice
        self.servicetype = servicetype
        self.option = option
        self.adapter = adapter
        self.supertype = supertype 
