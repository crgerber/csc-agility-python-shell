from base.TreeNode import TreeNodeBase
from actions.TreeNode import TreeNodeActions

class TreeNode(TreeNodeBase, TreeNodeActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, assetType=None, imagePath=None, parentPath=None, children=list(), label=None, parentType=None, folderAssetType=None, parentId=None, attributes=None, category=None, type=None, id=None, loaded=None, versionStatus=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param assetType: assetType minOccurs=0
        @type assetType: string
        @param imagePath: imagePath minOccurs=0
        @type imagePath: string
        @param parentPath: parentPath minOccurs=0
        @type parentPath: string
        @param children: children minOccurs=0 maxOccurs=unbounded
        @type children: TreeNode
        @param label: label minOccurs=0
        @type label: string
        @param parentType: parentType minOccurs=0
        @type parentType: string
        @param folderAssetType: folderAssetType minOccurs=0
        @type folderAssetType: string
        @param parentId: parentId minOccurs=0
        @type parentId: int
        @param attributes: attributes minOccurs=0
        @type attributes: string
        @param category: category minOccurs=0
        @type category: string
        @param type: type minOccurs=0
        @type type: string
        @param id: id minOccurs=0
        @type id: int
        @param loaded: loaded minOccurs=0
        @type loaded: boolean
        @param versionStatus: versionStatus minOccurs=0
        @type versionStatus: string
        '''
        TreeNodeBase.__init__(self, status=status, assetType=assetType, imagePath=imagePath, parentPath=parentPath, children=children, label=label, parentType=parentType, folderAssetType=folderAssetType, parentId=parentId, attributes=attributes, category=category, type=type, id=id, loaded=loaded, versionStatus=versionStatus)
