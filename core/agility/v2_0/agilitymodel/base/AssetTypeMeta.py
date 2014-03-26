from core.agility.common.AgilityModelBase import AgilityModelBase


class AssetTypeMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, applicableAssignmentType=list(), supportedEventType=list(), displayName='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'applicableAssignmentType': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'applicableAssignmentType', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayName', 'native': True}, 'supportedEventType': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'supportedEventType', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.applicableAssignmentType = applicableAssignmentType
        self.supportedEventType = supportedEventType
        self.displayName = displayName
        self.name = name 
