from base.ExecuteScriptResponse import ExecuteScriptResponseBase
from actions.ExecuteScriptResponse import ExecuteScriptResponseActions

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
