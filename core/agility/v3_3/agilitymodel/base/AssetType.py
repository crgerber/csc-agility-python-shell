from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class AssetTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, destconnection=[], srcconnection=[], displayname=None, entitytablename='', propertydefinition=[], allowextensions=False, global_=False, methoddefinition=[], propertydefinitiongroup=[], custom=False, propertydefinitionreference=[], hassubtypes=False, objectreference=[], entityclassname=None, usedtype=None, supertype=None, super=[], editor=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'destConnection': {'maxOccurs': 'unbounded', 'type': 'ConnectionDefinition', 'name': 'destconnection', 'minOccurs': '0', 'native': False}, 'global': {'type': 'boolean', 'name': 'global_', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'entityTableName': {'type': 'string', 'name': 'entitytablename', 'native': True}, 'propertyDefinition': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'propertydefinition', 'minOccurs': '0', 'native': False}, 'allowExtensions': {'type': 'boolean', 'name': 'allowextensions', 'native': True}, 'srcConnection': {'maxOccurs': 'unbounded', 'type': 'ConnectionDefinition', 'name': 'srcconnection', 'minOccurs': '0', 'native': False}, 'methodDefinition': {'maxOccurs': 'unbounded', 'type': 'MethodDefinition', 'name': 'methoddefinition', 'minOccurs': '0', 'native': False}, 'hasSubTypes': {'type': 'boolean', 'name': 'hassubtypes', 'native': True}, 'custom': {'type': 'boolean', 'name': 'custom', 'native': True}, 'propertyDefinitionReference': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinitionReference', 'name': 'propertydefinitionreference', 'minOccurs': '0', 'native': False}, 'propertyDefinitionGroup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'propertydefinitiongroup', 'minOccurs': '0', 'native': False}, 'objectReference': {'maxOccurs': 'unbounded', 'type': 'ObjectReference', 'name': 'objectreference', 'minOccurs': '0', 'native': False}, 'entityClassName': {'type': 'string', 'name': 'entityclassname', 'minOccurs': '0', 'native': True}, 'useDtype': {'type': 'boolean', 'name': 'usedtype', 'minOccurs': '0', 'native': True}, 'superType': {'type': 'Link', 'name': 'supertype', 'minOccurs': '0', 'native': False}, 'super': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'super', 'minOccurs': '0', 'native': False}, 'editor': {'maxOccurs': 'unbounded', 'type': 'Editor', 'name': 'editor', 'minOccurs': '0', 'native': False}})
        self.destconnection = destconnection
        self.srcconnection = srcconnection
        self.displayname = displayname
        self.entitytablename = entitytablename
        self.propertydefinition = propertydefinition
        self.allowextensions = allowextensions
        self.global_ = global_
        self.methoddefinition = methoddefinition
        self.propertydefinitiongroup = propertydefinitiongroup
        self.custom = custom
        self.propertydefinitionreference = propertydefinitionreference
        self.hassubtypes = hassubtypes
        self.objectreference = objectreference
        self.entityclassname = entityclassname
        self.usedtype = usedtype
        self.supertype = supertype
        self.super = super
        self.editor = editor 
