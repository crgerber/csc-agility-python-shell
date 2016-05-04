from base.GetVariableRequest import GetVariableRequestBase
from actions.GetVariableRequest import GetVariableRequestActions

class GetVariableRequest(GetVariableRequestBase, GetVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, variablesources=[], valuesources=[]):
        '''
        Constructor
        @param variablesources: variablesources minOccurs=0 maxOccurs=unbounded
        @type variablesources: Link
        @param valuesources: valuesources minOccurs=0 maxOccurs=unbounded
        @type valuesources: Link
        '''
        GetVariableRequestBase.__init__(self, variablesources=variablesources, valuesources=valuesources)
