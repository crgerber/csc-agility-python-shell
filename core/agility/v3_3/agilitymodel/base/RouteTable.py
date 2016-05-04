from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, route=[], routetableid=None, vpcid=None, mainassociationid=None, association=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'route': {'maxOccurs': 'unbounded', 'type': 'RouteTableRoute', 'name': 'route', 'minOccurs': '0', 'native': False}, 'vpcId': {'type': 'string', 'name': 'vpcid', 'minOccurs': '0', 'native': True}, 'routeTableId': {'type': 'string', 'name': 'routetableid', 'minOccurs': '0', 'native': True}, 'association': {'maxOccurs': 'unbounded', 'type': 'RouteTableAssociation', 'name': 'association', 'minOccurs': '0', 'native': False}, 'mainAssociationId': {'type': 'string', 'name': 'mainassociationid', 'minOccurs': '0', 'native': True}})
        self.route = route
        self.routetableid = routetableid
        self.vpcid = vpcid
        self.mainassociationid = mainassociationid
        self.association = association 
