from core.agility.v3_3.agilitymodel.base.ExecuteScriptRequest import ExecuteScriptRequestBase
from core.agility.v3_3.agilitymodel.actions.ExecuteScriptRequest import ExecuteScriptRequestActions

class ExecuteScriptRequest(ExecuteScriptRequestBase, ExecuteScriptRequestActions):
    '''
    classdocs
    '''
    def __init__(self, script=None, instance=None):
        '''
        Constructor
        @param script: script
        @type script: Script
        @param instance: instance
        @type instance: Instance
        '''
        ExecuteScriptRequestBase.__init__(self, script=script, instance=instance)
