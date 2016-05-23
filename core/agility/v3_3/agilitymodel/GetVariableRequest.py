from core.agility.v3_3.agilitymodel.base.GetVariableRequest import GetVariableRequestBase
from core.agility.v3_3.agilitymodel.actions.GetVariableRequest import GetVariableRequestActions

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
