from core.agility.v3_3.agilitymodel.base.TreeNode import TreeNodeBase
from core.agility.v3_3.agilitymodel.actions.TreeNode import TreeNodeActions

class TreeNode(TreeNodeBase, TreeNodeActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, assettype=None, imagepath=None, parentpath=None, children=[], label=None, parenttype=None, folderassettype=None, parentid=None, attributes=None, category=None, type=None, id=None, loaded=None, versionstatus=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param assettype: assettype minOccurs=0
        @type assettype: string
        @param imagepath: imagepath minOccurs=0
        @type imagepath: string
        @param parentpath: parentpath minOccurs=0
        @type parentpath: string
        @param children: children minOccurs=0 maxOccurs=unbounded
        @type children: TreeNode
        @param label: label minOccurs=0
        @type label: string
        @param parenttype: parenttype minOccurs=0
        @type parenttype: string
        @param folderassettype: folderassettype minOccurs=0
        @type folderassettype: string
        @param parentid: parentid minOccurs=0
        @type parentid: int
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
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        '''
        TreeNodeBase.__init__(self, status=status, assettype=assettype, imagepath=imagepath, parentpath=parentpath, children=children, label=label, parenttype=parenttype, folderassettype=folderassettype, parentid=parentid, attributes=attributes, category=category, type=type, id=id, loaded=loaded, versionstatus=versionstatus)
