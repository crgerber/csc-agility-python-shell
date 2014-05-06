from core.agility.v3_0.agilitymodel.base.InputVariableList import InputVariableListBase
from core.agility.v3_0.agilitymodel.actions.InputVariableList import InputVariableListActions

class InputVariableList(InputVariableListBase, InputVariableListActions):
    '''
    classdocs
    '''
    def __init__(self, inputvariable=[]):
        '''
        Constructor
        @param inputvariable: inputvariable minOccurs=0 maxOccurs=unbounded
        @type inputvariable: InputVariable
        '''
        InputVariableListBase.__init__(self, inputvariable=inputvariable)
