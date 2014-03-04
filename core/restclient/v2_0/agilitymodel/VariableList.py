from core.restclient.v2_0.agilitymodel.base.VariableList import VariableListBase
from core.restclient.v2_0.agilitymodel.actions.VariableList import VariableListActions

class VariableList(VariableListBase, VariableListActions):
    '''
    classdocs
    '''
    def __init__(self, variable=list()):
        '''
        Constructor
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: Variable
        '''
        VariableListBase.__init__(self, variable=variable)
