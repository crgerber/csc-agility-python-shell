from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableAssociationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, subnetid=None, main=None, routetableid=None, associationid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'subnetId': {'type': 'string', 'name': 'subnetid', 'minOccurs': '0', 'native': True}, 'routeTableId': {'type': 'string', 'name': 'routetableid', 'minOccurs': '0', 'native': True}, 'main': {'type': 'boolean', 'name': 'main', 'minOccurs': '0', 'native': True}, 'associationId': {'type': 'string', 'name': 'associationid', 'minOccurs': '0', 'native': True}})
        self.subnetid = subnetid
        self.main = main
        self.routetableid = routetableid
        self.associationid = associationid 
