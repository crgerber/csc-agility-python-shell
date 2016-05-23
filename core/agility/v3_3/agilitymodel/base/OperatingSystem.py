from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class OperatingSystemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, operatingsystemtype=None, displayname=None, parentoperatingsystem=None, effectivefilesystems=[], filesystems=[], mgmtscriptgroup=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'operatingSystemType': {'name': 'operatingsystemtype', 'minOccurs': '0', 'native': False, 'type': 'OperatingSystemType'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'parentOperatingSystem': {'name': 'parentoperatingsystem', 'native': False, 'type': 'Link'}, 'mgmtScriptGroup': {'name': 'mgmtscriptgroup', 'native': False, 'type': 'Link'}, 'fileSystems': {'name': 'filesystems', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'FileSystem'}, 'effectiveFileSystems': {'name': 'effectivefilesystems', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'FileSystem'}})
        self.operatingsystemtype = operatingsystemtype
        self.displayname = displayname
        self.parentoperatingsystem = parentoperatingsystem
        self.effectivefilesystems = effectivefilesystems
        self.filesystems = filesystems
        self.mgmtscriptgroup = mgmtscriptgroup 
