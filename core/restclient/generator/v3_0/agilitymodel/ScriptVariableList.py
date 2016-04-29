from .base.ScriptVariableList import ScriptVariableListBase
from .actions.ScriptVariableList import ScriptVariableListActions

class ScriptVariableList(ScriptVariableListBase, ScriptVariableListActions):
    '''
    classdocs
    '''
    def __init__(self, scriptvariable=[]):
        '''
        Constructor
        @param scriptvariable: scriptvariable minOccurs=0 maxOccurs=unbounded
        @type scriptvariable: ScriptVariable
        '''
        ScriptVariableListBase.__init__(self, scriptvariable=scriptvariable)
