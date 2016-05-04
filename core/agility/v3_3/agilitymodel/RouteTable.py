from base.RouteTable import RouteTableBase
from actions.RouteTable import RouteTableActions

class RouteTable(RouteTableBase, RouteTableActions):
    '''
    classdocs
    '''
    def __init__(self, route=[], routetableid=None, vpcid=None, mainassociationid=None, association=[]):
        '''
        Constructor
        @param route: route minOccurs=0 maxOccurs=unbounded
        @type route: RouteTableRoute
        @param routetableid: routetableid minOccurs=0
        @type routetableid: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param mainassociationid: mainassociationid minOccurs=0
        @type mainassociationid: string
        @param association: association minOccurs=0 maxOccurs=unbounded
        @type association: RouteTableAssociation
        '''
        RouteTableBase.__init__(self, route=route, routetableid=routetableid, vpcid=vpcid, mainassociationid=mainassociationid, association=association)
