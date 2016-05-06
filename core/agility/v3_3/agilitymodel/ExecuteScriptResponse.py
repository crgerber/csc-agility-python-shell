from core.agility.v3_3.agilitymodel.base.ExecuteScriptResponse import ExecuteScriptResponseBase
from core.agility.v3_3.agilitymodel.actions.ExecuteScriptResponse import ExecuteScriptResponseActions

class ExecuteScriptResponse(ExecuteScriptResponseBase, ExecuteScriptResponseActions):
    '''
    classdocs
    '''
    def __init__(self, scriptstatus=None):
        '''
        Constructor
        @param scriptstatus: scriptstatus minOccurs=0
        @type scriptstatus: ScriptStatus
        '''
        ExecuteScriptResponseBase.__init__(self, scriptstatus=scriptstatus)
