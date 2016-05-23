from core.agility.common.AgilityModelBase import AgilityModelBase

class InputVariableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, valueset=[], variablesource=None, variable=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'valueSet': {'name': 'valueset', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'VariableValueSet'}, 'variableSource': {'name': 'variablesource', 'minOccurs': '0', 'native': False, 'type': 'Asset'}, 'variable': {'name': 'variable', 'native': False, 'type': 'PropertyDefinition'}})
        self.valueset = valueset
        self.variablesource = variablesource
        self.variable = variable 
