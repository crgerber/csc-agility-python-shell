from .base.InputVariable import InputVariableBase
from .actions.InputVariable import InputVariableActions

class InputVariable(InputVariableBase, InputVariableActions):
    '''
    classdocs
    '''
    def __init__(self, variable=None, variablesource=None, valueset=[]):
        '''
        Constructor
        @param variable: variable
        @type variable: PropertyDefinition
        @param variablesource: variablesource minOccurs=0
        @type variablesource: Asset
        @param valueset: valueset minOccurs=0 maxOccurs=unbounded
        @type valueset: VariableValueSet
        '''
        InputVariableBase.__init__(self, variable=variable, variablesource=variablesource, valueset=valueset)
