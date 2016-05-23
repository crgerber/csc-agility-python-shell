from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class IPAMValidationRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, crudoperation=None, serviceprovider=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'crudOperation': {'name': 'crudoperation', 'native': False, 'type': 'IPAMValidationCRUDType'}, 'serviceProvider': {'name': 'serviceprovider', 'minOccurs': '0', 'native': False, 'type': 'ServiceProvider'}})
        self.crudoperation = crudoperation
        self.serviceprovider = serviceprovider 
