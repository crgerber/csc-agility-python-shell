from ApiRequest import ApiRequestBase

class GetVariableRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, variablesources=[], valuesources=[]):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variableSources': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'variablesources', 'minOccurs': '0', 'native': False}, 'valueSources': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'valuesources', 'minOccurs': '0', 'native': False}})
        self.variablesources = variablesources
        self.valuesources = valuesources 
