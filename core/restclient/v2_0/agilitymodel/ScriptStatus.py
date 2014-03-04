from core.restclient.v2_0.agilitymodel.base.ScriptStatus import ScriptStatusBase
from core.restclient.v2_0.agilitymodel.actions.ScriptStatus import ScriptStatusActions

class ScriptStatus(ScriptStatusBase, ScriptStatusActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, name=None, stdout='', timestamp=None, completed=None, runStatus=None, scriptId=None, stderr='', id=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: int
        @param name: name minOccurs=0
        @type name: string
        @param stdout: stdout
        @type stdout: string
        @param timestamp: timestamp minOccurs=0
        @type timestamp: long
        @param completed: completed minOccurs=0
        @type completed: long
        @param runStatus: runStatus minOccurs=0
        @type runStatus: ScriptState
        @param scriptId: scriptId minOccurs=0
        @type scriptId: int
        @param stderr: stderr
        @type stderr: string
        @param id: id minOccurs=0
        @type id: int
        '''
        ScriptStatusBase.__init__(self, status=status, name=name, stdout=stdout, timestamp=timestamp, completed=completed, runStatus=runStatus, scriptId=scriptId, stderr=stderr, id=id)
