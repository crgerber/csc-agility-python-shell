from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class OperatingSystemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, operatingsystemtype=None, effectivefilesystems=[], parentoperatingsystem=None, filesystems=[], displayname=None, mgmtscriptgroup=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'operatingSystemType': {'native': False, 'name': 'operatingsystemtype', 'minOccurs': '0', 'type': 'OperatingSystemType'}, 'effectiveFileSystems': {'maxOccurs': 'unbounded', 'native': False, 'name': 'effectivefilesystems', 'minOccurs': '0', 'type': 'FileSystem'}, 'fileSystems': {'maxOccurs': 'unbounded', 'native': False, 'name': 'filesystems', 'minOccurs': '0', 'type': 'FileSystem'}, 'parentOperatingSystem': {'native': False, 'name': 'parentoperatingsystem', 'type': 'Link'}, 'mgmtScriptGroup': {'native': False, 'name': 'mgmtscriptgroup', 'type': 'Link'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}})
        self.operatingsystemtype = operatingsystemtype
        self.effectivefilesystems = effectivefilesystems
        self.parentoperatingsystem = parentoperatingsystem
        self.filesystems = filesystems
        self.displayname = displayname
        self.mgmtscriptgroup = mgmtscriptgroup 
