from core.agility.v3_3.agilitymodel.base.RouteTableRoute import RouteTableRouteBase
from core.agility.v3_3.agilitymodel.actions.RouteTableRoute import RouteTableRouteActions

class RouteTableRoute(RouteTableRouteBase, RouteTableRouteActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, destinationcidrblock=None, origin=None, targetgateway=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param destinationcidrblock: destinationcidrblock minOccurs=0
        @type destinationcidrblock: string
        @param origin: origin minOccurs=0
        @type origin: string
        @param targetgateway: targetgateway minOccurs=0
        @type targetgateway: string
        '''
        RouteTableRouteBase.__init__(self, status=status, destinationcidrblock=destinationcidrblock, origin=origin, targetgateway=targetgateway)
