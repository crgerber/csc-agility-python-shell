from base.AssetType import AssetTypeBase
from actions.AssetType import AssetTypeActions

class AssetType(AssetTypeBase, AssetTypeActions):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, entityTableName='', propertyDefinition=list(), global_=False, custom=False, propertyDefinitionReference=list(), propertyDefinitionGroup=list(), objectReference=list(), entityClassName=None, useDtype=None):
        '''
        Constructor
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param entityTableName: entityTableName
        @type entityTableName: string
        @param propertyDefinition: propertyDefinition minOccurs=0 maxOccurs=unbounded
        @type propertyDefinition: PropertyDefinition
        @param global_: global_
        @type global_: boolean
        @param custom: custom
        @type custom: boolean
        @param propertyDefinitionReference: propertyDefinitionReference minOccurs=0 maxOccurs=unbounded
        @type propertyDefinitionReference: PropertyDefinitionReference
        @param propertyDefinitionGroup: propertyDefinitionGroup minOccurs=0 maxOccurs=unbounded
        @type propertyDefinitionGroup: Link
        @param objectReference: objectReference minOccurs=0 maxOccurs=unbounded
        @type objectReference: ObjectReference
        @param entityClassName: entityClassName minOccurs=0
        @type entityClassName: string
        @param useDtype: useDtype minOccurs=0
        @type useDtype: boolean
        '''
        AssetTypeBase.__init__(self, displayName=displayName, entityTableName=entityTableName, propertyDefinition=propertyDefinition, global_=global_, custom=custom, propertyDefinitionReference=propertyDefinitionReference, propertyDefinitionGroup=propertyDefinitionGroup, objectReference=objectReference, entityClassName=entityClassName, useDtype=useDtype)
