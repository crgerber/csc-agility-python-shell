from core.agility.common.AgilityModelBase import AgilityModelBase

class ExecuteScriptResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, scriptstatus=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'scriptStatus': {'type': 'ScriptStatus', 'name': 'scriptstatus', 'minOccurs': '0', 'native': False}})
        self.scriptstatus = scriptstatus 
