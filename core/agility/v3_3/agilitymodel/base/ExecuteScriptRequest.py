from ApiRequest import ApiRequestBase

class ExecuteScriptRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, script=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instance': {'type': 'Instance', 'name': 'instance', 'native': False}, 'script': {'type': 'Script', 'name': 'script', 'native': False}})
        self.instance = instance
        self.script = script 
