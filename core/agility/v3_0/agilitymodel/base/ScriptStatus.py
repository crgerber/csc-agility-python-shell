from core.agility.common.AgilityModelBase import AgilityModelBase


class ScriptStatusBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, name=None, stdout='', timestamp=None, completed=None, runstatus=None, scriptid=None, stderr='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'int', 'name': 'status', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'stdout': {'type': 'string', 'name': 'stdout', 'native': True}, 'timestamp': {'type': 'long', 'name': 'timestamp', 'minOccurs': '0', 'native': True}, 'completed': {'type': 'long', 'name': 'completed', 'minOccurs': '0', 'native': True}, 'runStatus': {'type': 'ScriptState', 'name': 'runstatus', 'minOccurs': '0', 'native': False}, 'scriptId': {'type': 'int', 'name': 'scriptid', 'minOccurs': '0', 'native': True}, 'stderr': {'type': 'string', 'name': 'stderr', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.name = name
        self.stdout = stdout
        self.timestamp = timestamp
        self.completed = completed
        self.runstatus = runstatus
        self.scriptid = scriptid
        self.stderr = stderr
        self.id = id 
