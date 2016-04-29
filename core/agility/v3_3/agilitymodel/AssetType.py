from core.agility.v3_3.agilitymodel.base.AssetType import AssetTypeBase
from core.agility.v3_3.agilitymodel.actions.AssetType import AssetTypeActions

class AssetType(AssetTypeBase, AssetTypeActions):
    '''
    classdocs
    '''
    def __init__(self, destconnection=[], super=[], global_=False, propertydefinitiongroup=[], propertydefinitionreference=[], custom=False, editor=[], displayname=None, hassubtypes=False, entitytablename='', entityclassname=None, usedtype=None, allowextensions=False, propertydefinition=[], objectreference=[], srcconnection=[], methoddefinition=[], supertype=None):
        '''
        Constructor
        @param destconnection: destconnection minOccurs=0 maxOccurs=unbounded
        @type destconnection: ConnectionDefinition
        @param super: super minOccurs=0 maxOccurs=unbounded
        @type super: Link
        @param global_: global_
        @type global_: boolean
        @param propertydefinitiongroup: propertydefinitiongroup minOccurs=0 maxOccurs=unbounded
        @type propertydefinitiongroup: Link
        @param propertydefinitionreference: propertydefinitionreference minOccurs=0 maxOccurs=unbounded
        @type propertydefinitionreference: PropertyDefinitionReference
        @param custom: custom
        @type custom: boolean
        @param editor: editor minOccurs=0 maxOccurs=unbounded
        @type editor: Editor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param hassubtypes: hassubtypes
        @type hassubtypes: boolean
        @param entitytablename: entitytablename
        @type entitytablename: string
        @param entityclassname: entityclassname minOccurs=0
        @type entityclassname: string
        @param usedtype: usedtype minOccurs=0
        @type usedtype: boolean
        @param allowextensions: allowextensions
        @type allowextensions: boolean
        @param propertydefinition: propertydefinition minOccurs=0 maxOccurs=unbounded
        @type propertydefinition: PropertyDefinition
        @param objectreference: objectreference minOccurs=0 maxOccurs=unbounded
        @type objectreference: ObjectReference
        @param srcconnection: srcconnection minOccurs=0 maxOccurs=unbounded
        @type srcconnection: ConnectionDefinition
        @param methoddefinition: methoddefinition minOccurs=0 maxOccurs=unbounded
        @type methoddefinition: MethodDefinition
        @param supertype: supertype minOccurs=0
        @type supertype: Link
        '''
        AssetTypeBase.__init__(self, destconnection=destconnection, super=super, global_=global_, propertydefinitiongroup=propertydefinitiongroup, propertydefinitionreference=propertydefinitionreference, custom=custom, editor=editor, displayname=displayname, hassubtypes=hassubtypes, entitytablename=entitytablename, entityclassname=entityclassname, usedtype=usedtype, allowextensions=allowextensions, propertydefinition=propertydefinition, objectreference=objectreference, srcconnection=srcconnection, methoddefinition=methoddefinition, supertype=supertype)
