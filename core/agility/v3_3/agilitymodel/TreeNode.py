from core.agility.v3_3.agilitymodel.base.TreeNode import TreeNodeBase
from core.agility.v3_3.agilitymodel.actions.TreeNode import TreeNodeActions

class TreeNode(TreeNodeBase, TreeNodeActions):
    '''
    classdocs
    '''
    def __init__(self, attributes=None, parentid=None, folderassettype=None, parenttype=None, label=None, assettype=None, versionstatus=None, children=[], loaded=None, parentpath=None, id=None, imagepath=None, category=None, type=None, status=None):
        '''
        Constructor
        @param attributes: attributes minOccurs=0
        @type attributes: string
        @param parentid: parentid minOccurs=0
        @type parentid: int
        @param folderassettype: folderassettype minOccurs=0
        @type folderassettype: string
        @param parenttype: parenttype minOccurs=0
        @type parenttype: string
        @param label: label minOccurs=0
        @type label: string
        @param assettype: assettype minOccurs=0
        @type assettype: string
        @param versionstatus: versionstatus minOccurs=0
        @type versionstatus: string
        @param children: children minOccurs=0 maxOccurs=unbounded
        @type children: TreeNode
        @param loaded: loaded minOccurs=0
        @type loaded: boolean
        @param parentpath: parentpath minOccurs=0
        @type parentpath: string
        @param id: id minOccurs=0
        @type id: int
        @param imagepath: imagepath minOccurs=0
        @type imagepath: string
        @param category: category minOccurs=0
        @type category: string
        @param type: type minOccurs=0
        @type type: string
        @param status: status minOccurs=0
        @type status: string
        '''
        TreeNodeBase.__init__(self, attributes=attributes, parentid=parentid, folderassettype=folderassettype, parenttype=parenttype, label=label, assettype=assettype, versionstatus=versionstatus, children=children, loaded=loaded, parentpath=parentpath, id=id, imagepath=imagepath, category=category, type=type, status=status)
