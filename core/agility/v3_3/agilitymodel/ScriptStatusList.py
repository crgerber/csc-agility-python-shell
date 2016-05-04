from base.ScriptStatusList import ScriptStatusListBase
from actions.ScriptStatusList import ScriptStatusListActions

class ScriptStatusList(ScriptStatusListBase, ScriptStatusListActions):
    '''
    classdocs
    '''
    def __init__(self, scriptstatus=[]):
        '''
        Constructor
        @param scriptstatus: scriptstatus minOccurs=0 maxOccurs=unbounded
        @type scriptstatus: ScriptStatus
        '''
        ScriptStatusListBase.__init__(self, scriptstatus=scriptstatus)
