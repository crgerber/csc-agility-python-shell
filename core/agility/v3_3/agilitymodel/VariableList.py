from core.agility.v3_3.agilitymodel.base.VariableList import VariableListBase
from core.agility.v3_3.agilitymodel.actions.VariableList import VariableListActions

class VariableList(VariableListBase, VariableListActions):
    '''
    classdocs
    '''
    def __init__(self, variable=[]):
        '''
        Constructor
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: Variable
        '''
        VariableListBase.__init__(self, variable=variable)
