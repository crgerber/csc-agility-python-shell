from core.agility.v3_3.agilitymodel.base.ApiResponse import ApiResponseBase

class CloudPropertyResponseBase(ApiResponseBase):
    '''
    classdocs
    '''
    def __init__(self, value=False):
        ApiResponseBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'type': 'boolean', 'name': 'value', 'native': True}})
        self.value = value 
