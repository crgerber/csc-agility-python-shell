from base.InputVariableList import InputVariableListBase
from actions.InputVariableList import InputVariableListActions

class InputVariableList(InputVariableListBase, InputVariableListActions):
    '''
    classdocs
    '''
    def __init__(self, inputVariable=list()):
        '''
        Constructor
        @param inputVariable: inputVariable minOccurs=0 maxOccurs=unbounded
        @type inputVariable: InputVariable
        '''
        InputVariableListBase.__init__(self, inputVariable=inputVariable)
