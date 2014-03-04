from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class AssetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assetType=None, usedByAssets=list(), importMode=None, uuid=None, detailedAssetPath=None, tags=None, assetProperties=list(), top=False, importDirectives=None, name=None, lifecycleVersion=None, Assetlist=list(), Asset=list(), removable=None, lifecycleLastComment=None, assetPath=None, lifecycleState=None, id=None, applicationType=None, description=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'type': 'Link', 'name': 'assetType', 'minOccurs': '0', 'native': False}, 'usedByAssets': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'usedByAssets', 'minOccurs': '0', 'native': False}, 'importMode': {'type': 'ImportMode', 'name': 'importMode', 'minOccurs': '0', 'native': False}, 'uuid': {'type': 'string', 'name': 'uuid', 'minOccurs': '0', 'native': True}, 'tags': {'type': 'string', 'name': 'tags', 'minOccurs': '0', 'native': True}, 'assetProperties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'assetProperties', 'minOccurs': '0', 'native': False}, 'top': {'type': 'boolean', 'name': 'top', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}, 'importDirectives': {'type': 'ImportDirectives', 'name': 'importDirectives', 'minOccurs': '0', 'native': False}, 'lifecycleVersion': {'type': 'int', 'name': 'lifecycleVersion', 'minOccurs': '0', 'native': True}, 'Assetlist': {'maxOccurs': 'unbounded', 'type': 'Assetlist', 'name': 'Assetlist', 'minOccurs': '0', 'native': False}, 'lifecycleState': {'type': 'string', 'name': 'lifecycleState', 'minOccurs': '0', 'native': True}, 'Asset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'Asset', 'minOccurs': '0', 'native': False}, 'removable': {'type': 'boolean', 'name': 'removable', 'minOccurs': '0', 'native': True}, 'lifecycleLastComment': {'type': 'string', 'name': 'lifecycleLastComment', 'minOccurs': '0', 'native': True}, 'detailedAssetPath': {'type': 'string', 'name': 'detailedAssetPath', 'minOccurs': '0', 'native': True}, 'assetPath': {'type': 'string', 'name': 'assetPath', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'applicationType': {'type': 'string', 'name': 'applicationType', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.assetType = assetType
        self.usedByAssets = usedByAssets
        self.importMode = importMode
        self.uuid = uuid
        self.detailedAssetPath = detailedAssetPath
        self.tags = tags
        self.assetProperties = assetProperties
        self.top = top
        self.importDirectives = importDirectives
        self.name = name
        self.lifecycleVersion = lifecycleVersion
        self.Assetlist = Assetlist
        self.Asset = Asset
        self.removable = removable
        self.lifecycleLastComment = lifecycleLastComment
        self.assetPath = assetPath
        self.lifecycleState = lifecycleState
        self.id = id
        self.applicationType = applicationType
        self.description = description 
