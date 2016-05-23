from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableAssociationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, subnetid=None, associationid=None, main=None, routetableid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'subnetId': {'name': 'subnetid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'associationId': {'name': 'associationid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'main': {'name': 'main', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'routeTableId': {'name': 'routetableid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.subnetid = subnetid
        self.associationid = associationid
        self.main = main
        self.routetableid = routetableid 
