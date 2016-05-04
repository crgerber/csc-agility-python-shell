from core.agility.common.AgilityModelBase import AgilityModelBase

class RouteTableRouteBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, destinationcidrblock=None, targetgateway=None, origin=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'destinationCidrBlock': {'type': 'string', 'name': 'destinationcidrblock', 'minOccurs': '0', 'native': True}, 'targetGateway': {'type': 'string', 'name': 'targetgateway', 'minOccurs': '0', 'native': True}, 'origin': {'type': 'string', 'name': 'origin', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.destinationcidrblock = destinationcidrblock
        self.targetgateway = targetgateway
        self.origin = origin 
