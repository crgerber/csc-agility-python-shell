from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class MgmtScriptBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, mgmtscripttype='', script=None, filesystem=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'mgmtScriptType': {'native': True, 'name': 'mgmtscripttype', 'type': 'string'}, 'script': {'native': False, 'name': 'script', 'type': 'Link'}, 'fileSystem': {'native': False, 'name': 'filesystem', 'minOccurs': '0', 'type': 'Link'}})
        self.mgmtscripttype = mgmtscripttype
        self.script = script
        self.filesystem = filesystem 
