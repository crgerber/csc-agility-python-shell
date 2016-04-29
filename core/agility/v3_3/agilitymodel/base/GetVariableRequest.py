from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class GetVariableRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, valuesources=[], variablesources=[]):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'valueSources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'valuesources', 'minOccurs': '0', 'type': 'Link'}, 'variableSources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variablesources', 'minOccurs': '0', 'type': 'Link'}})
        self.valuesources = valuesources
        self.variablesources = variablesources 
