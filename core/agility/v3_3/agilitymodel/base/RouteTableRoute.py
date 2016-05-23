from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableRouteBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, destinationcidrblock=None, origin=None, targetgateway=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'targetGateway': {'name': 'targetgateway', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'origin': {'name': 'origin', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'destinationCidrBlock': {'name': 'destinationcidrblock', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.status = status
        self.destinationcidrblock = destinationcidrblock
        self.origin = origin
        self.targetgateway = targetgateway 
