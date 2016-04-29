from .base.VariableList import VariableListBase
from .actions.VariableList import VariableListActions

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
