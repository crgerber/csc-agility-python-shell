from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetTypeMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, supportedeventtype=[], name='', displayname='', applicableassignmenttype=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'supportedEventType': {'maxOccurs': 'unbounded', 'native': True, 'name': 'supportedeventtype', 'minOccurs': '0', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'displayName': {'native': True, 'name': 'displayname', 'type': 'string'}, 'applicableAssignmentType': {'maxOccurs': 'unbounded', 'native': True, 'name': 'applicableassignmenttype', 'minOccurs': '0', 'type': 'string'}})
        self.supportedeventtype = supportedeventtype
        self.name = name
        self.displayname = displayname
        self.applicableassignmenttype = applicableassignmenttype 
