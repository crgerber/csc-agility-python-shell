from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class ExecuteScriptRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, script=None, instance=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'script': {'native': False, 'name': 'script', 'type': 'Script'}, 'instance': {'native': False, 'name': 'instance', 'type': 'Instance'}})
        self.script = script
        self.instance = instance 
