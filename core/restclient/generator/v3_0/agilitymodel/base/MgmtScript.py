from Asset import AssetBase

class MgmtScriptBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, script=None, mgmtscripttype='', filesystem=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'fileSystem': {'type': 'Link', 'name': 'filesystem', 'minOccurs': '0', 'native': False}, 'mgmtScriptType': {'type': 'string', 'name': 'mgmtscripttype', 'native': True}, 'script': {'type': 'Link', 'name': 'script', 'native': False}})
        self.script = script
        self.mgmtscripttype = mgmtscripttype
        self.filesystem = filesystem 
