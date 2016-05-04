from ApiRequest import ApiRequestBase

class IPAMValidationRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, serviceprovider=None, crudoperation=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceProvider': {'type': 'ServiceProvider', 'name': 'serviceprovider', 'minOccurs': '0', 'native': False}, 'crudOperation': {'type': 'IPAMValidationCRUDType', 'name': 'crudoperation', 'native': False}})
        self.serviceprovider = serviceprovider
        self.crudoperation = crudoperation 
