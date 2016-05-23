from core.agility.v3_3.agilitymodel.base.ApiResponse import ApiResponseBase

class GetVariableResponseBase(ApiResponseBase):
    '''
    classdocs
    '''
    def __init__(self, inputvariable=[]):
        ApiResponseBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'inputVariable': {'name': 'inputvariable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'InputVariable'}})
        self.inputvariable = inputvariable 
