from core.agility.v3_0.agilitymodel.base.InputVariableRequest import InputVariableRequestBase
from core.agility.v3_0.agilitymodel.actions.InputVariableRequest import InputVariableRequestActions

class InputVariableRequest(InputVariableRequestBase, InputVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, variablesource=[], valuesource=[]):
        '''
        Constructor
        @param variablesource: variablesource minOccurs=0 maxOccurs=unbounded
        @type variablesource: Link
        @param valuesource: valuesource minOccurs=0 maxOccurs=unbounded
        @type valuesource: Link
        '''
        InputVariableRequestBase.__init__(self, variablesource=variablesource, valuesource=valuesource)
