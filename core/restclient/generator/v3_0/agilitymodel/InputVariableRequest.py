from .base.InputVariableRequest import InputVariableRequestBase
from .actions.InputVariableRequest import InputVariableRequestActions

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
