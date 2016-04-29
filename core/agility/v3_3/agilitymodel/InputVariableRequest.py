from core.agility.v3_3.agilitymodel.base.InputVariableRequest import InputVariableRequestBase
from core.agility.v3_3.agilitymodel.actions.InputVariableRequest import InputVariableRequestActions

class InputVariableRequest(InputVariableRequestBase, InputVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, valuesource=[], variablesource=[], excludepackagescripts=False):
        '''
        Constructor
        @param valuesource: valuesource minOccurs=0 maxOccurs=unbounded
        @type valuesource: Link
        @param variablesource: variablesource minOccurs=0 maxOccurs=unbounded
        @type variablesource: Link
        @param excludepackagescripts: excludepackagescripts
        @type excludepackagescripts: boolean
        '''
        InputVariableRequestBase.__init__(self, valuesource=valuesource, variablesource=variablesource, excludepackagescripts=excludepackagescripts)
