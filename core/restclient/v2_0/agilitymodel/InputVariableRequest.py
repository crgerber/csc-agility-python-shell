from core.restclient.v2_0.agilitymodel.base.InputVariableRequest import InputVariableRequestBase
from core.restclient.v2_0.agilitymodel.actions.InputVariableRequest import InputVariableRequestActions

class InputVariableRequest(InputVariableRequestBase, InputVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, variableSource=list(), valueSource=list()):
        '''
        Constructor
        @param variableSource: variableSource minOccurs=0 maxOccurs=unbounded
        @type variableSource: Link
        @param valueSource: valueSource minOccurs=0 maxOccurs=unbounded
        @type valueSource: Link
        '''
        InputVariableRequestBase.__init__(self, variableSource=variableSource, valueSource=valueSource)
