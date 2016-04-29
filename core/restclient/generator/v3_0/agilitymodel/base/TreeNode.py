from .AgilityModelBase import AgilityModelBase

class TreeNodeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, assettype=None, imagepath=None, parentpath=None, children=[], label=None, parenttype=None, folderassettype=None, parentid=None, attributes=None, category=None, type=None, id=None, loaded=None, versionstatus=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'assetType': {'type': 'string', 'name': 'assettype', 'minOccurs': '0', 'native': True}, 'imagePath': {'type': 'string', 'name': 'imagepath', 'minOccurs': '0', 'native': True}, 'parentId': {'type': 'int', 'name': 'parentid', 'minOccurs': '0', 'native': True}, 'label': {'type': 'string', 'name': 'label', 'minOccurs': '0', 'native': True}, 'parentType': {'type': 'string', 'name': 'parenttype', 'minOccurs': '0', 'native': True}, 'folderAssetType': {'type': 'string', 'name': 'folderassettype', 'minOccurs': '0', 'native': True}, 'parentPath': {'type': 'string', 'name': 'parentpath', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'attributes': {'type': 'string', 'name': 'attributes', 'minOccurs': '0', 'native': True}, 'category': {'type': 'string', 'name': 'category', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'children': {'maxOccurs': 'unbounded', 'type': 'TreeNode', 'name': 'children', 'minOccurs': '0', 'native': False}, 'loaded': {'type': 'boolean', 'name': 'loaded', 'minOccurs': '0', 'native': True}, 'versionStatus': {'type': 'string', 'name': 'versionstatus', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.assettype = assettype
        self.imagepath = imagepath
        self.parentpath = parentpath
        self.children = children
        self.label = label
        self.parenttype = parenttype
        self.folderassettype = folderassettype
        self.parentid = parentid
        self.attributes = attributes
        self.category = category
        self.type = type
        self.id = id
        self.loaded = loaded
        self.versionstatus = versionstatus 
