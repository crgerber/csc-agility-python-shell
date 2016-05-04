from core.agility.common.AgilityModelBase import AgilityModelBase

class InputVariableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variable=None, variablesource=None, valueset=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'type': 'PropertyDefinition', 'name': 'variable', 'native': False}, 'variableSource': {'type': 'Asset', 'name': 'variablesource', 'minOccurs': '0', 'native': False}, 'valueSet': {'maxOccurs': 'unbounded', 'type': 'VariableValueSet', 'name': 'valueset', 'minOccurs': '0', 'native': False}})
        self.variable = variable
        self.variablesource = variablesource
        self.valueset = valueset 
