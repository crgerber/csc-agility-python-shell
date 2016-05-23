from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mainassociationid=None, association=[], vpcid=None, routetableid=None, route=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'mainAssociationId': {'name': 'mainassociationid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'association': {'name': 'association', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'RouteTableAssociation'}, 'routeTableId': {'name': 'routetableid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'vpcId': {'name': 'vpcid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'route': {'name': 'route', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'RouteTableRoute'}})
        self.mainassociationid = mainassociationid
        self.association = association
        self.vpcid = vpcid
        self.routetableid = routetableid
        self.route = route 
