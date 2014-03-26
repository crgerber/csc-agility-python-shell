from base.Variable import VariableBase
from actions.Variable import VariableActions

class Variable(VariableBase, VariableActions):
    '''
    classdocs
    '''
    def __init__(self, value=None):
        '''
        Constructor
        @param value: value minOccurs=0
        @type value: string
        '''
        VariableBase.__init__(self, value=value)
