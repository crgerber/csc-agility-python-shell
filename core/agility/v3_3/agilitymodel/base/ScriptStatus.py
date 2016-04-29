from core.agility.common.AgilityModelBase import AgilityModelBase

class ScriptStatusBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, completed=None, runstatus=None, timestamp=None, stdout='', name=None, scriptid=None, status=None, id=None, stderr=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'completed': {'native': True, 'name': 'completed', 'minOccurs': '0', 'type': 'long'}, 'runStatus': {'native': False, 'name': 'runstatus', 'minOccurs': '0', 'type': 'ScriptState'}, 'timestamp': {'native': True, 'name': 'timestamp', 'minOccurs': '0', 'type': 'long'}, 'stdout': {'native': True, 'name': 'stdout', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'scriptId': {'native': True, 'name': 'scriptid', 'minOccurs': '0', 'type': 'int'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'int'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'stderr': {'native': True, 'name': 'stderr', 'type': 'string'}})
        self.completed = completed
        self.runstatus = runstatus
        self.timestamp = timestamp
        self.stdout = stdout
        self.name = name
        self.scriptid = scriptid
        self.status = status
        self.id = id
        self.stderr = stderr 
