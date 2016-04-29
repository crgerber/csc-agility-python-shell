from core.agility.v3_3.agilitymodel.base.GetVariableRequest import GetVariableRequestBase
from core.agility.v3_3.agilitymodel.actions.GetVariableRequest import GetVariableRequestActions

class GetVariableRequest(GetVariableRequestBase, GetVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, valuesources=[], variablesources=[]):
        '''
        Constructor
        @param valuesources: valuesources minOccurs=0 maxOccurs=unbounded
        @type valuesources: Link
        @param variablesources: variablesources minOccurs=0 maxOccurs=unbounded
        @type variablesources: Link
        '''
        GetVariableRequestBase.__init__(self, valuesources=valuesources, variablesources=variablesources)
