from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class OperatingSystemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, parentoperatingsystem=None, mgmtscriptgroup=None, filesystems=[], operatingsystemtype=None, effectivefilesystems=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'parentOperatingSystem': {'type': 'Link', 'name': 'parentoperatingsystem', 'native': False}, 'mgmtScriptGroup': {'type': 'Link', 'name': 'mgmtscriptgroup', 'native': False}, 'fileSystems': {'maxOccurs': 'unbounded', 'type': 'FileSystem', 'name': 'filesystems', 'minOccurs': '0', 'native': False}, 'operatingSystemType': {'type': 'OperatingSystemType', 'name': 'operatingsystemtype', 'minOccurs': '0', 'native': False}, 'effectiveFileSystems': {'maxOccurs': 'unbounded', 'type': 'FileSystem', 'name': 'effectivefilesystems', 'minOccurs': '0', 'native': False}})
        self.displayname = displayname
        self.parentoperatingsystem = parentoperatingsystem
        self.mgmtscriptgroup = mgmtscriptgroup
        self.filesystems = filesystems
        self.operatingsystemtype = operatingsystemtype
        self.effectivefilesystems = effectivefilesystems 
