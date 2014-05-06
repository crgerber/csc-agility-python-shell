from core.agility.common.AgilityModelBase import AgilityModelBase


class InputVariableRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variableSource=list(), valueSource=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variableSource': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'variableSource', 'minOccurs': '0', 'native': False}, 'valueSource': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'valueSource', 'minOccurs': '0', 'native': False}})
        self.variableSource = variableSource
        self.valueSource = valueSource 
