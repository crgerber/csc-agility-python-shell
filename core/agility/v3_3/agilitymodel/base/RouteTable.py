from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, routetableid=None, mainassociationid=None, route=[], association=[], vpcid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'routeTableId': {'native': True, 'name': 'routetableid', 'minOccurs': '0', 'type': 'string'}, 'mainAssociationId': {'native': True, 'name': 'mainassociationid', 'minOccurs': '0', 'type': 'string'}, 'route': {'maxOccurs': 'unbounded', 'native': False, 'name': 'route', 'minOccurs': '0', 'type': 'RouteTableRoute'}, 'vpcId': {'native': True, 'name': 'vpcid', 'minOccurs': '0', 'type': 'string'}, 'association': {'maxOccurs': 'unbounded', 'native': False, 'name': 'association', 'minOccurs': '0', 'type': 'RouteTableAssociation'}})
        self.routetableid = routetableid
        self.mainassociationid = mainassociationid
        self.route = route
        self.association = association
        self.vpcid = vpcid 
