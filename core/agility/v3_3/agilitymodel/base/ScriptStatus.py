from core.agility.common.AgilityModelBase import AgilityModelBase

class ScriptStatusBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, timestamp=None, id=None, runstatus=None, completed=None, status=None, stdout='', name=None, scriptid=None, stderr=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'timestamp': {'name': 'timestamp', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'stdout': {'name': 'stdout', 'native': True, 'type': 'string'}, 'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'scriptId': {'name': 'scriptid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'completed': {'name': 'completed', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'runStatus': {'name': 'runstatus', 'minOccurs': '0', 'native': False, 'type': 'ScriptState'}, 'stderr': {'name': 'stderr', 'native': True, 'type': 'string'}})
        self.timestamp = timestamp
        self.id = id
        self.runstatus = runstatus
        self.completed = completed
        self.status = status
        self.stdout = stdout
        self.name = name
        self.scriptid = scriptid
        self.stderr = stderr 
