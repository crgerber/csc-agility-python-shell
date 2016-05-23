from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class AssetTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, custom=False, srcconnection=[], displayname=None, allowextensions=False, supertype=None, entitytablename='', global_=False, propertydefinitionreference=[], entityclassname=None, usedtype=None, hassubtypes=False, objectreference=[], editor=[], methoddefinition=[], propertydefinition=[], destconnection=[], super=[], propertydefinitiongroup=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'custom': {'name': 'custom', 'native': True, 'type': 'boolean'}, 'srcConnection': {'name': 'srcconnection', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ConnectionDefinition'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'superType': {'name': 'supertype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'allowExtensions': {'name': 'allowextensions', 'native': True, 'type': 'boolean'}, 'global': {'name': 'global_', 'native': True, 'type': 'boolean'}, 'propertyDefinition': {'name': 'propertydefinition', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'entityClassName': {'name': 'entityclassname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'useDtype': {'name': 'usedtype', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'hasSubTypes': {'name': 'hassubtypes', 'native': True, 'type': 'boolean'}, 'propertyDefinitionGroup': {'name': 'propertydefinitiongroup', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'destConnection': {'name': 'destconnection', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ConnectionDefinition'}, 'editor': {'name': 'editor', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Editor'}, 'methodDefinition': {'name': 'methoddefinition', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'MethodDefinition'}, 'propertyDefinitionReference': {'name': 'propertydefinitionreference', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinitionReference'}, 'objectReference': {'name': 'objectreference', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ObjectReference'}, 'super': {'name': 'super', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'entityTableName': {'name': 'entitytablename', 'native': True, 'type': 'string'}})
        self.custom = custom
        self.srcconnection = srcconnection
        self.displayname = displayname
        self.allowextensions = allowextensions
        self.supertype = supertype
        self.entitytablename = entitytablename
        self.global_ = global_
        self.propertydefinitionreference = propertydefinitionreference
        self.entityclassname = entityclassname
        self.usedtype = usedtype
        self.hassubtypes = hassubtypes
        self.objectreference = objectreference
        self.editor = editor
        self.methoddefinition = methoddefinition
        self.propertydefinition = propertydefinition
        self.destconnection = destconnection
        self.super = super
        self.propertydefinitiongroup = propertydefinitiongroup 
