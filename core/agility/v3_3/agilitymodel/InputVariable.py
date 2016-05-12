from core.agility.v3_3.agilitymodel.base.InputVariable import InputVariableBase
from core.agility.v3_3.agilitymodel.actions.InputVariable import InputVariableActions

class InputVariable(InputVariableBase, InputVariableActions):
    '''
    classdocs
    '''
    def __init__(self, variablesource=None, variable=None, valueset=[]):
        '''
        Constructor
        @param variablesource: variablesource minOccurs=0
        @type variablesource: Asset
        @param variable: variable
        @type variable: PropertyDefinition
        @param valueset: valueset minOccurs=0 maxOccurs=unbounded
        @type valueset: VariableValueSet
        '''
        InputVariableBase.__init__(self, variablesource=variablesource, variable=variable, valueset=valueset)