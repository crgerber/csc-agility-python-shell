from core.restclient.v2_0.agilitymodel.base.AssetTypeMeta import AssetTypeMetaBase
from core.restclient.v2_0.agilitymodel.actions.AssetTypeMeta import AssetTypeMetaActions

class AssetTypeMeta(AssetTypeMetaBase, AssetTypeMetaActions):
    '''
    classdocs
    '''
    def __init__(self, applicableAssignmentType=list(), supportedEventType=list(), displayName='', name=''):
        '''
        Constructor
        @param applicableAssignmentType: applicableAssignmentType minOccurs=0 maxOccurs=unbounded
        @type applicableAssignmentType: string
        @param supportedEventType: supportedEventType minOccurs=0 maxOccurs=unbounded
        @type supportedEventType: string
        @param displayName: displayName
        @type displayName: string
        @param name: name
        @type name: string
        '''
        AssetTypeMetaBase.__init__(self, applicableAssignmentType=applicableAssignmentType, supportedEventType=supportedEventType, displayName=displayName, name=name)
