from AgilityModelBase import AgilityModelBase

class TreeNodeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, assetType=None, imagePath=None, parentPath=None, children=list(), label=None, parentType=None, folderAssetType=None, parentId=None, attributes=None, category=None, type=None, id=None, loaded=None, versionStatus=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'assetType': {'type': 'string', 'name': 'assetType', 'minOccurs': '0', 'native': True}, 'imagePath': {'type': 'string', 'name': 'imagePath', 'minOccurs': '0', 'native': True}, 'parentId': {'type': 'int', 'name': 'parentId', 'minOccurs': '0', 'native': True}, 'label': {'type': 'string', 'name': 'label', 'minOccurs': '0', 'native': True}, 'parentType': {'type': 'string', 'name': 'parentType', 'minOccurs': '0', 'native': True}, 'folderAssetType': {'type': 'string', 'name': 'folderAssetType', 'minOccurs': '0', 'native': True}, 'parentPath': {'type': 'string', 'name': 'parentPath', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'attributes': {'type': 'string', 'name': 'attributes', 'minOccurs': '0', 'native': True}, 'category': {'type': 'string', 'name': 'category', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'children': {'maxOccurs': 'unbounded', 'type': 'TreeNode', 'name': 'children', 'minOccurs': '0', 'native': False}, 'loaded': {'type': 'boolean', 'name': 'loaded', 'minOccurs': '0', 'native': True}, 'versionStatus': {'type': 'string', 'name': 'versionStatus', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.assetType = assetType
        self.imagePath = imagePath
        self.parentPath = parentPath
        self.children = children
        self.label = label
        self.parentType = parentType
        self.folderAssetType = folderAssetType
        self.parentId = parentId
        self.attributes = attributes
        self.category = category
        self.type = type
        self.id = id
        self.loaded = loaded
        self.versionStatus = versionStatus 
