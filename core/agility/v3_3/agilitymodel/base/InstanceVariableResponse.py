from core.agility.v3_3.agilitymodel.base.ApiResponse import ApiResponseBase

class InstanceVariableResponseBase(ApiResponseBase):
    '''
    classdocs
    '''
    def __init__(self, variables=[]):
        ApiResponseBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'Variable'}})
        self.variables = variables 
