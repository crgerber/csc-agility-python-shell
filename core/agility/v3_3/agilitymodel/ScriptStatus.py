from core.agility.v3_3.agilitymodel.base.ScriptStatus import ScriptStatusBase
from core.agility.v3_3.agilitymodel.actions.ScriptStatus import ScriptStatusActions

class ScriptStatus(ScriptStatusBase, ScriptStatusActions):
    '''
    classdocs
    '''
    def __init__(self, timestamp=None, id=None, runstatus=None, completed=None, status=None, stdout='', name=None, scriptid=None, stderr=''):
        '''
        Constructor
        @param timestamp: timestamp minOccurs=0
        @type timestamp: long
        @param id: id minOccurs=0
        @type id: int
        @param runstatus: runstatus minOccurs=0
        @type runstatus: ScriptState
        @param completed: completed minOccurs=0
        @type completed: long
        @param status: status minOccurs=0
        @type status: int
        @param stdout: stdout
        @type stdout: string
        @param name: name minOccurs=0
        @type name: string
        @param scriptid: scriptid minOccurs=0
        @type scriptid: int
        @param stderr: stderr
        @type stderr: string
        '''
        ScriptStatusBase.__init__(self, timestamp=timestamp, id=id, runstatus=runstatus, completed=completed, status=status, stdout=stdout, name=name, scriptid=scriptid, stderr=stderr)
