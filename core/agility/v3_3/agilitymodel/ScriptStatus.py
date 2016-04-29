from core.agility.v3_3.agilitymodel.base.ScriptStatus import ScriptStatusBase
from core.agility.v3_3.agilitymodel.actions.ScriptStatus import ScriptStatusActions

class ScriptStatus(ScriptStatusBase, ScriptStatusActions):
    '''
    classdocs
    '''
    def __init__(self, completed=None, runstatus=None, timestamp=None, stdout='', name=None, scriptid=None, status=None, id=None, stderr=''):
        '''
        Constructor
        @param completed: completed minOccurs=0
        @type completed: long
        @param runstatus: runstatus minOccurs=0
        @type runstatus: ScriptState
        @param timestamp: timestamp minOccurs=0
        @type timestamp: long
        @param stdout: stdout
        @type stdout: string
        @param name: name minOccurs=0
        @type name: string
        @param scriptid: scriptid minOccurs=0
        @type scriptid: int
        @param status: status minOccurs=0
        @type status: int
        @param id: id minOccurs=0
        @type id: int
        @param stderr: stderr
        @type stderr: string
        '''
        ScriptStatusBase.__init__(self, completed=completed, runstatus=runstatus, timestamp=timestamp, stdout=stdout, name=name, scriptid=scriptid, status=status, id=id, stderr=stderr)
