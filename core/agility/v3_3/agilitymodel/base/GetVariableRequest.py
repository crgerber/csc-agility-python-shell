from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class GetVariableRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, variablesources=[], valuesources=[]):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variableSources': {'name': 'variablesources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'valueSources': {'name': 'valuesources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.variablesources = variablesources
        self.valuesources = valuesources 
