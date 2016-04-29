from core.agility.v3_3.agilitymodel.base.TreeNode import TreeNodeBase
from core.agility.v3_3.agilitymodel.actions.TreeNode import TreeNodeActions

class TreeNode(TreeNodeBase, TreeNodeActions):
    '''
    classdocs
    '''
    def __init__(self, loaded=None, parenttype=None, label=None, folderassettype=None, status=None, id=None, parentid=None, category=None, children=[], assettype=None, parentpath=None, attributes=None, type=None, imagepath=None, versionstatus=None):
        '''
        Constructor
        @param loaded: loaded minOccurs=0
        @type loaded: boolean
        @param parenttype: parenttype minOccurs=0
        @type parenttype: string
        @param label: label minOccurs=0
        @type label: string
        @param folderassettype: folderassettype minOccurs=0
        @type folderassettype: string
        @param status: status minOccurs=0
        @type status: string
        @param id: id minOccurs=0
        @type id: int
        @param parentid: parentid minOccurs=0
        @type parentid: int
        @param category: category minOccurs=0
        @type category: string
        @param children: children minOccurs=0 maxOccurs=unbounded
        @type children: TreeNode
        @param assettype: assettype minOccurs=0
        @type assettype: string
        @param parentpath: parentpath minOccurs=0
        @type parentpath: string
        @param attributes: attributes minOccurs=0
        @type attributes: string
        @param type: type minOccurs=0
        @type type: string
        @param imagepath: imagepath minOccurs=0
        @type imagepath: string
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        '''
        TreeNodeBase.__init__(self, loaded=loaded, parenttype=parenttype, label=label, folderassettype=folderassettype, status=status, id=id, parentid=parentid, category=category, children=children, assettype=assettype, parentpath=parentpath, attributes=attributes, type=type, imagepath=imagepath, versionstatus=versionstatus)
