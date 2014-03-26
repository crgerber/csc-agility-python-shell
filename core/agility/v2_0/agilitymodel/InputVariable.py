from core.agility.v2_0.agilitymodel.base.InputVariable import InputVariableBase
from core.agility.v2_0.agilitymodel.actions.InputVariable import InputVariableActions

class InputVariable(InputVariableBase, InputVariableActions):
    '''
    classdocs
    '''
    def __init__(self, variable=None, variableSource=None, valueSet=list()):
        '''
        Constructor
        @param variable: variable
        @type variable: PropertyDefinition
        @param variableSource: variableSource minOccurs=0
        @type variableSource: Asset
        @param valueSet: valueSet minOccurs=0 maxOccurs=unbounded
        @type valueSet: VariableValueSet
        '''
        InputVariableBase.__init__(self, variable=variable, variableSource=variableSource, valueSet=valueSet)
