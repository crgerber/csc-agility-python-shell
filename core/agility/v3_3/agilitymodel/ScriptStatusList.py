from core.agility.v3_3.agilitymodel.base.ScriptStatusList import ScriptStatusListBase
from core.agility.v3_3.agilitymodel.actions.ScriptStatusList import ScriptStatusListActions

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
