from base.GetVariableResponse import GetVariableResponseBase
from actions.GetVariableResponse import GetVariableResponseActions

class GetVariableResponse(GetVariableResponseBase, GetVariableResponseActions):
    '''
    classdocs
    '''
    def __init__(self, inputvariable=[]):
        '''
        Constructor
        @param inputvariable: inputvariable minOccurs=0 maxOccurs=unbounded
        @type inputvariable: InputVariable
        '''
        GetVariableResponseBase.__init__(self, inputvariable=inputvariable)
