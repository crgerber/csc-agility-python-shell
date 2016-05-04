from core.agility.v3_3.agilitymodel.base.ExecuteScriptRequest import ExecuteScriptRequestBase
from core.agility.v3_3.agilitymodel.actions.ExecuteScriptRequest import ExecuteScriptRequestActions

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
