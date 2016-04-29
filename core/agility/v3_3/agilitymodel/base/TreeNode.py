from core.agility.common.AgilityModelBase import AgilityModelBase

class TreeNodeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, loaded=None, parenttype=None, label=None, folderassettype=None, status=None, id=None, parentid=None, category=None, children=[], assettype=None, parentpath=None, attributes=None, type=None, imagepath=None, versionstatus=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'loaded': {'native': True, 'name': 'loaded', 'minOccurs': '0', 'type': 'boolean'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'label': {'native': True, 'name': 'label', 'minOccurs': '0', 'type': 'string'}, 'folderAssetType': {'native': True, 'name': 'folderassettype', 'minOccurs': '0', 'type': 'string'}, 'children': {'maxOccurs': 'unbounded', 'native': False, 'name': 'children', 'minOccurs': '0', 'type': 'TreeNode'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'parentId': {'native': True, 'name': 'parentid', 'minOccurs': '0', 'type': 'int'}, 'category': {'native': True, 'name': 'category', 'minOccurs': '0', 'type': 'string'}, 'assetType': {'native': True, 'name': 'assettype', 'minOccurs': '0', 'type': 'string'}, 'versionStatus': {'native': True, 'name': 'versionstatus', 'minOccurs': '0', 'type': 'string'}, 'attributes': {'native': True, 'name': 'attributes', 'minOccurs': '0', 'type': 'string'}, 'parentPath': {'native': True, 'name': 'parentpath', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}, 'parentType': {'native': True, 'name': 'parenttype', 'minOccurs': '0', 'type': 'string'}, 'imagePath': {'native': True, 'name': 'imagepath', 'minOccurs': '0', 'type': 'string'}})
        self.loaded = loaded
        self.parenttype = parenttype
        self.label = label
        self.folderassettype = folderassettype
        self.status = status
        self.id = id
        self.parentid = parentid
        self.category = category
        self.children = children
        self.assettype = assettype
        self.parentpath = parentpath
        self.attributes = attributes
        self.type = type
        self.imagepath = imagepath
        self.versionstatus = versionstatus 
