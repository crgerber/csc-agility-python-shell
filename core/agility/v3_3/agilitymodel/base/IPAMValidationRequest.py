from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class IPAMValidationRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, serviceprovider=None, crudoperation=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceProvider': {'native': False, 'name': 'serviceprovider', 'minOccurs': '0', 'type': 'ServiceProvider'}, 'crudOperation': {'native': False, 'name': 'crudoperation', 'type': 'IPAMValidationCRUDType'}})
        self.serviceprovider = serviceprovider
        self.crudoperation = crudoperation 
