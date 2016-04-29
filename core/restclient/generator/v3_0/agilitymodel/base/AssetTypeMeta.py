from .AgilityModelBase import AgilityModelBase

class AssetTypeMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, applicableassignmenttype=[], supportedeventtype=[], displayname='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'applicableAssignmentType': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'applicableassignmenttype', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayname', 'native': True}, 'supportedEventType': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'supportedeventtype', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.applicableassignmenttype = applicableassignmenttype
        self.supportedeventtype = supportedeventtype
        self.displayname = displayname
        self.name = name 
