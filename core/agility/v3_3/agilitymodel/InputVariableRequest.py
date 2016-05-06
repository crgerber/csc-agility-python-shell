from core.agility.v3_3.agilitymodel.base.InputVariableRequest import InputVariableRequestBase
from core.agility.v3_3.agilitymodel.actions.InputVariableRequest import InputVariableRequestActions

class InputVariableRequest(InputVariableRequestBase, InputVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, variablesource=[], excludepackagescripts=False, valuesource=[]):
        '''
        Constructor
        @param variablesource: variablesource minOccurs=0 maxOccurs=unbounded
        @type variablesource: Link
        @param excludepackagescripts: excludepackagescripts
        @type excludepackagescripts: boolean
        @param valuesource: valuesource minOccurs=0 maxOccurs=unbounded
        @type valuesource: Link
        '''
        InputVariableRequestBase.__init__(self, variablesource=variablesource, excludepackagescripts=excludepackagescripts, valuesource=valuesource)
