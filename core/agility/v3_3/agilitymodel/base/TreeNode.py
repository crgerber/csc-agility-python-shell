from core.agility.common.AgilityModelBase import AgilityModelBase

class TreeNodeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, attributes=None, parentid=None, folderassettype=None, parenttype=None, label=None, assettype=None, versionstatus=None, children=[], loaded=None, parentpath=None, id=None, imagepath=None, category=None, type=None, status=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attributes': {'name': 'attributes', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'parentId': {'name': 'parentid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'folderAssetType': {'name': 'folderassettype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'loaded': {'name': 'loaded', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'assetType': {'name': 'assettype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'versionStatus': {'name': 'versionstatus', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'children': {'name': 'children', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'TreeNode'}, 'label': {'name': 'label', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'parentPath': {'name': 'parentpath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'imagePath': {'name': 'imagepath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'category': {'name': 'category', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'parentType': {'name': 'parenttype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.attributes = attributes
        self.parentid = parentid
        self.folderassettype = folderassettype
        self.parenttype = parenttype
        self.label = label
        self.assettype = assettype
        self.versionstatus = versionstatus
        self.children = children
        self.loaded = loaded
        self.parentpath = parentpath
        self.id = id
        self.imagepath = imagepath
        self.category = category
        self.type = type
        self.status = status 
