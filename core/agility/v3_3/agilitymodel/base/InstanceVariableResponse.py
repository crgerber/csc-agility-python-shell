from ApiResponse import ApiResponseBase

class InstanceVariableResponseBase(ApiResponseBase):
    '''
    classdocs
    '''
    def __init__(self, variables=[]):
        ApiResponseBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variables': {'maxOccurs': 'unbounded', 'type': 'Variable', 'name': 'variables', 'minOccurs': '0', 'native': False}})
        self.variables = variables 
