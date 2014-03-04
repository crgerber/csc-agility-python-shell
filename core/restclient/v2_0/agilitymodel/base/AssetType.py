from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class AssetTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, entityTableName='', propertyDefinition=list(), global_=False, custom=False, propertyDefinitionReference=list(), propertyDefinitionGroup=list(), objectReference=list(), entityClassName=None, useDtype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'entityTableName': {'type': 'string', 'name': 'entityTableName', 'native': True}, 'propertyDefinition': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'propertyDefinition', 'minOccurs': '0', 'native': False}, 'global': {'type': 'boolean', 'name': 'global_', 'native': True}, 'custom': {'type': 'boolean', 'name': 'custom', 'native': True}, 'propertyDefinitionReference': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinitionReference', 'name': 'propertyDefinitionReference', 'minOccurs': '0', 'native': False}, 'propertyDefinitionGroup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'propertyDefinitionGroup', 'minOccurs': '0', 'native': False}, 'objectReference': {'maxOccurs': 'unbounded', 'type': 'ObjectReference', 'name': 'objectReference', 'minOccurs': '0', 'native': False}, 'entityClassName': {'type': 'string', 'name': 'entityClassName', 'minOccurs': '0', 'native': True}, 'useDtype': {'type': 'boolean', 'name': 'useDtype', 'minOccurs': '0', 'native': True}})
        self.displayName = displayName
        self.entityTableName = entityTableName
        self.propertyDefinition = propertyDefinition
        self.global_ = global_
        self.custom = custom
        self.propertyDefinitionReference = propertyDefinitionReference
        self.propertyDefinitionGroup = propertyDefinitionGroup
        self.objectReference = objectReference
        self.entityClassName = entityClassName
        self.useDtype = useDtype 
