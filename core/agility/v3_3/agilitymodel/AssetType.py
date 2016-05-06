from core.agility.v3_3.agilitymodel.base.AssetType import AssetTypeBase
from core.agility.v3_3.agilitymodel.actions.AssetType import AssetTypeActions

class AssetType(AssetTypeBase, AssetTypeActions):
    '''
    classdocs
    '''
    def __init__(self, destconnection=[], srcconnection=[], displayname=None, entitytablename='', propertydefinition=[], allowextensions=False, global_=False, methoddefinition=[], propertydefinitiongroup=[], custom=False, propertydefinitionreference=[], hassubtypes=False, objectreference=[], entityclassname=None, usedtype=None, supertype=None, super=[], editor=[]):
        '''
        Constructor
        @param destconnection: destconnection minOccurs=0 maxOccurs=unbounded
        @type destconnection: ConnectionDefinition
        @param srcconnection: srcconnection minOccurs=0 maxOccurs=unbounded
        @type srcconnection: ConnectionDefinition
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param entitytablename: entitytablename
        @type entitytablename: string
        @param propertydefinition: propertydefinition minOccurs=0 maxOccurs=unbounded
        @type propertydefinition: PropertyDefinition
        @param allowextensions: allowextensions
        @type allowextensions: boolean
        @param global_: global_
        @type global_: boolean
        @param methoddefinition: methoddefinition minOccurs=0 maxOccurs=unbounded
        @type methoddefinition: MethodDefinition
        @param propertydefinitiongroup: propertydefinitiongroup minOccurs=0 maxOccurs=unbounded
        @type propertydefinitiongroup: Link
        @param custom: custom
        @type custom: boolean
        @param propertydefinitionreference: propertydefinitionreference minOccurs=0 maxOccurs=unbounded
        @type propertydefinitionreference: PropertyDefinitionReference
        @param hassubtypes: hassubtypes
        @type hassubtypes: boolean
        @param objectreference: objectreference minOccurs=0 maxOccurs=unbounded
        @type objectreference: ObjectReference
        @param entityclassname: entityclassname minOccurs=0
        @type entityclassname: string
        @param usedtype: usedtype minOccurs=0
        @type usedtype: boolean
        @param supertype: supertype minOccurs=0
        @type supertype: Link
        @param super: super minOccurs=0 maxOccurs=unbounded
        @type super: Link
        @param editor: editor minOccurs=0 maxOccurs=unbounded
        @type editor: Editor
        '''
        AssetTypeBase.__init__(self, destconnection=destconnection, srcconnection=srcconnection, displayname=displayname, entitytablename=entitytablename, propertydefinition=propertydefinition, allowextensions=allowextensions, global_=global_, methoddefinition=methoddefinition, propertydefinitiongroup=propertydefinitiongroup, custom=custom, propertydefinitionreference=propertydefinitionreference, hassubtypes=hassubtypes, objectreference=objectreference, entityclassname=entityclassname, usedtype=usedtype, supertype=supertype, super=super, editor=editor)
