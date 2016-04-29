from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class AssetTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, destconnection=[], super=[], global_=False, propertydefinitiongroup=[], propertydefinitionreference=[], custom=False, editor=[], displayname=None, hassubtypes=False, entitytablename='', entityclassname=None, usedtype=None, allowextensions=False, propertydefinition=[], objectreference=[], srcconnection=[], methoddefinition=[], supertype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'destConnection': {'maxOccurs': 'unbounded', 'native': False, 'name': 'destconnection', 'minOccurs': '0', 'type': 'ConnectionDefinition'}, 'methodDefinition': {'maxOccurs': 'unbounded', 'native': False, 'name': 'methoddefinition', 'minOccurs': '0', 'type': 'MethodDefinition'}, 'global': {'native': True, 'name': 'global_', 'type': 'boolean'}, 'propertyDefinitionGroup': {'maxOccurs': 'unbounded', 'native': False, 'name': 'propertydefinitiongroup', 'minOccurs': '0', 'type': 'Link'}, 'propertyDefinitionReference': {'maxOccurs': 'unbounded', 'native': False, 'name': 'propertydefinitionreference', 'minOccurs': '0', 'type': 'PropertyDefinitionReference'}, 'custom': {'native': True, 'name': 'custom', 'type': 'boolean'}, 'editor': {'maxOccurs': 'unbounded', 'native': False, 'name': 'editor', 'minOccurs': '0', 'type': 'Editor'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'hasSubTypes': {'native': True, 'name': 'hassubtypes', 'type': 'boolean'}, 'entityTableName': {'native': True, 'name': 'entitytablename', 'type': 'string'}, 'entityClassName': {'native': True, 'name': 'entityclassname', 'minOccurs': '0', 'type': 'string'}, 'useDtype': {'native': True, 'name': 'usedtype', 'minOccurs': '0', 'type': 'boolean'}, 'propertyDefinition': {'maxOccurs': 'unbounded', 'native': False, 'name': 'propertydefinition', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'superType': {'native': False, 'name': 'supertype', 'minOccurs': '0', 'type': 'Link'}, 'allowExtensions': {'native': True, 'name': 'allowextensions', 'type': 'boolean'}, 'srcConnection': {'maxOccurs': 'unbounded', 'native': False, 'name': 'srcconnection', 'minOccurs': '0', 'type': 'ConnectionDefinition'}, 'super': {'maxOccurs': 'unbounded', 'native': False, 'name': 'super', 'minOccurs': '0', 'type': 'Link'}, 'objectReference': {'maxOccurs': 'unbounded', 'native': False, 'name': 'objectreference', 'minOccurs': '0', 'type': 'ObjectReference'}})
        self.destconnection = destconnection
        self.super = super
        self.global_ = global_
        self.propertydefinitiongroup = propertydefinitiongroup
        self.propertydefinitionreference = propertydefinitionreference
        self.custom = custom
        self.editor = editor
        self.displayname = displayname
        self.hassubtypes = hassubtypes
        self.entitytablename = entitytablename
        self.entityclassname = entityclassname
        self.usedtype = usedtype
        self.allowextensions = allowextensions
        self.propertydefinition = propertydefinition
        self.objectreference = objectreference
        self.srcconnection = srcconnection
        self.methoddefinition = methoddefinition
        self.supertype = supertype 
