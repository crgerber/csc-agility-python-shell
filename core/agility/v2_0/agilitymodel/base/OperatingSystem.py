from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class OperatingSystemBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, effectiveFileSystems=list(), fileSystems=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'effectiveFileSystems': {'maxOccurs': 'unbounded', 'type': 'FileSystem', 'name': 'effectiveFileSystems', 'minOccurs': '0', 'native': False}, 'fileSystems': {'maxOccurs': 'unbounded', 'type': 'FileSystem', 'name': 'fileSystems', 'minOccurs': '0', 'native': False}})
        self.displayName = displayName
        self.effectiveFileSystems = effectiveFileSystems
        self.fileSystems = fileSystems 
