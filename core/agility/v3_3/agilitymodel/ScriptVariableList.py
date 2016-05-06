from core.agility.v3_3.agilitymodel.base.ScriptVariableList import ScriptVariableListBase
from core.agility.v3_3.agilitymodel.actions.ScriptVariableList import ScriptVariableListActions

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
