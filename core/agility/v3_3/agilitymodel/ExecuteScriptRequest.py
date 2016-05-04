from base.ExecuteScriptRequest import ExecuteScriptRequestBase
from actions.ExecuteScriptRequest import ExecuteScriptRequestActions

class ExecuteScriptRequest(ExecuteScriptRequestBase, ExecuteScriptRequestActions):
    '''
    classdocs
    '''
    def __init__(self, instance=None, script=None):
        '''
        Constructor
        @param instance: instance
        @type instance: Instance
        @param script: script
        @type script: Script
        '''
        ExecuteScriptRequestBase.__init__(self, instance=instance, script=script)
