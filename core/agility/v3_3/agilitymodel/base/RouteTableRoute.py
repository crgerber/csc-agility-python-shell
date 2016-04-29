from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableRouteBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, destinationcidrblock=None, origin=None, targetgateway=None, status=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'destinationCidrBlock': {'native': True, 'name': 'destinationcidrblock', 'minOccurs': '0', 'type': 'string'}, 'origin': {'native': True, 'name': 'origin', 'minOccurs': '0', 'type': 'string'}, 'targetGateway': {'native': True, 'name': 'targetgateway', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}})
        self.destinationcidrblock = destinationcidrblock
        self.origin = origin
        self.targetgateway = targetgateway
        self.status = status 
