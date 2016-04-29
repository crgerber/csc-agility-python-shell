from core.agility.common.AgilityModelBase import AgilityModelBase

class InputVariableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variablesource=None, variable=None, valueset=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variableSource': {'native': False, 'name': 'variablesource', 'minOccurs': '0', 'type': 'Asset'}, 'variable': {'native': False, 'name': 'variable', 'type': 'PropertyDefinition'}, 'valueSet': {'maxOccurs': 'unbounded', 'native': False, 'name': 'valueset', 'minOccurs': '0', 'type': 'VariableValueSet'}})
        self.variablesource = variablesource
        self.variable = variable
        self.valueset = valueset 
