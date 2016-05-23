from core.agility.v3_3.agilitymodel.base.AssetType import AssetTypeBase
from core.agility.v3_3.agilitymodel.actions.AssetType import AssetTypeActions

class AssetType(AssetTypeBase, AssetTypeActions):
    '''
    classdocs
    '''
    def __init__(self, custom=False, srcconnection=[], displayname=None, allowextensions=False, supertype=None, entitytablename='', global_=False, propertydefinitionreference=[], entityclassname=None, usedtype=None, hassubtypes=False, objectreference=[], editor=[], methoddefinition=[], propertydefinition=[], destconnection=[], super=[], propertydefinitiongroup=[]):
        '''
        Constructor
        @param custom: custom
        @type custom: boolean
        @param srcconnection: srcconnection minOccurs=0 maxOccurs=unbounded
        @type srcconnection: ConnectionDefinition
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param allowextensions: allowextensions
        @type allowextensions: boolean
        @param supertype: supertype minOccurs=0
        @type supertype: Link
        @param entitytablename: entitytablename
        @type entitytablename: string
        @param global_: global_
        @type global_: boolean
        @param propertydefinitionreference: propertydefinitionreference minOccurs=0 maxOccurs=unbounded
        @type propertydefinitionreference: PropertyDefinitionReference
        @param entityclassname: entityclassname minOccurs=0
        @type entityclassname: string
        @param usedtype: usedtype minOccurs=0
        @type usedtype: boolean
        @param hassubtypes: hassubtypes
        @type hassubtypes: boolean
        @param objectreference: objectreference minOccurs=0 maxOccurs=unbounded
        @type objectreference: ObjectReference
        @param editor: editor minOccurs=0 maxOccurs=unbounded
        @type editor: Editor
        @param methoddefinition: methoddefinition minOccurs=0 maxOccurs=unbounded
        @type methoddefinition: MethodDefinition
        @param propertydefinition: propertydefinition minOccurs=0 maxOccurs=unbounded
        @type propertydefinition: PropertyDefinition
        @param destconnection: destconnection minOccurs=0 maxOccurs=unbounded
        @type destconnection: ConnectionDefinition
        @param super: super minOccurs=0 maxOccurs=unbounded
        @type super: Link
        @param propertydefinitiongroup: propertydefinitiongroup minOccurs=0 maxOccurs=unbounded
        @type propertydefinitiongroup: Link
        '''
        AssetTypeBase.__init__(self, custom=custom, srcconnection=srcconnection, displayname=displayname, allowextensions=allowextensions, supertype=supertype, entitytablename=entitytablename, global_=global_, propertydefinitionreference=propertydefinitionreference, entityclassname=entityclassname, usedtype=usedtype, hassubtypes=hassubtypes, objectreference=objectreference, editor=editor, methoddefinition=methoddefinition, propertydefinition=propertydefinition, destconnection=destconnection, super=super, propertydefinitiongroup=propertydefinitiongroup)
