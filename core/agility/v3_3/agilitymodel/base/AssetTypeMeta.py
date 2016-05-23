from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetTypeMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', applicableassignmenttype=[], displayname='', supportedeventtype=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'applicableAssignmentType': {'name': 'applicableassignmenttype', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'displayName': {'name': 'displayname', 'native': True, 'type': 'string'}, 'supportedEventType': {'name': 'supportedeventtype', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.name = name
        self.applicableassignmenttype = applicableassignmenttype
        self.displayname = displayname
        self.supportedeventtype = supportedeventtype 
