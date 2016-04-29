from core.agility.v3_3.agilitymodel.base.RouteTableRoute import RouteTableRouteBase
from core.agility.v3_3.agilitymodel.actions.RouteTableRoute import RouteTableRouteActions

class RouteTableRoute(RouteTableRouteBase, RouteTableRouteActions):
    '''
    classdocs
    '''
    def __init__(self, destinationcidrblock=None, origin=None, targetgateway=None, status=None):
        '''
        Constructor
        @param destinationcidrblock: destinationcidrblock minOccurs=0
        @type destinationcidrblock: string
        @param origin: origin minOccurs=0
        @type origin: string
        @param targetgateway: targetgateway minOccurs=0
        @type targetgateway: string
        @param status: status minOccurs=0
        @type status: string
        '''
        RouteTableRouteBase.__init__(self, destinationcidrblock=destinationcidrblock, origin=origin, targetgateway=targetgateway, status=status)
