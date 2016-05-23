from core.agility.v3_3.agilitymodel.base.InputVariableRequest import InputVariableRequestBase
from core.agility.v3_3.agilitymodel.actions.InputVariableRequest import InputVariableRequestActions

class InputVariableRequest(InputVariableRequestBase, InputVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, excludepackagescripts=False, variablesource=[], valuesource=[]):
        '''
        Constructor
        @param excludepackagescripts: excludepackagescripts
        @type excludepackagescripts: boolean
        @param variablesource: variablesource minOccurs=0 maxOccurs=unbounded
        @type variablesource: Link
        @param valuesource: valuesource minOccurs=0 maxOccurs=unbounded
        @type valuesource: Link
        '''
        InputVariableRequestBase.__init__(self, excludepackagescripts=excludepackagescripts, variablesource=variablesource, valuesource=valuesource)
