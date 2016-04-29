from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableAssociationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, routetableid=None, subnetid=None, associationid=None, main=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'routeTableId': {'native': True, 'name': 'routetableid', 'minOccurs': '0', 'type': 'string'}, 'subnetId': {'native': True, 'name': 'subnetid', 'minOccurs': '0', 'type': 'string'}, 'associationId': {'native': True, 'name': 'associationid', 'minOccurs': '0', 'type': 'string'}, 'main': {'native': True, 'name': 'main', 'minOccurs': '0', 'type': 'boolean'}})
        self.routetableid = routetableid
        self.subnetid = subnetid
        self.associationid = associationid
        self.main = main 
