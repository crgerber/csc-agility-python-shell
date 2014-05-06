from Asset import AssetBase

class OperatingSystemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, mgmtscriptgroup=None, displayname=None, effectivefilesystems=[], filesystems=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'mgmtScriptGroup': {'type': 'Link', 'name': 'mgmtscriptgroup', 'native': False}, 'effectiveFileSystems': {'maxOccurs': 'unbounded', 'type': 'FileSystem', 'name': 'effectivefilesystems', 'minOccurs': '0', 'native': False}, 'fileSystems': {'maxOccurs': 'unbounded', 'type': 'FileSystem', 'name': 'filesystems', 'minOccurs': '0', 'native': False}})
        self.mgmtscriptgroup = mgmtscriptgroup
        self.displayname = displayname
        self.effectivefilesystems = effectivefilesystems
        self.filesystems = filesystems 
