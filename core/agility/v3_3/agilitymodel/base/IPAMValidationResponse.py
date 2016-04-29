from core.agility.v3_3.agilitymodel.base.ApiResponse import ApiResponseBase

class IPAMValidationResponseBase(ApiResponseBase):
    '''
    classdocs
    '''
    def __init__(self, errormessage=None):
        ApiResponseBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'errorMessage': {'native': True, 'name': 'errormessage', 'minOccurs': '0', 'type': 'string'}})
        self.errormessage = errormessage 
