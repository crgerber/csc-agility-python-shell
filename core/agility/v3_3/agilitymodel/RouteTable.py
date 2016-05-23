from core.agility.v3_3.agilitymodel.base.RouteTable import RouteTableBase
from core.agility.v3_3.agilitymodel.actions.RouteTable import RouteTableActions

class RouteTable(RouteTableBase, RouteTableActions):
    '''
    classdocs
    '''
    def __init__(self, mainassociationid=None, association=[], vpcid=None, routetableid=None, route=[]):
        '''
        Constructor
        @param mainassociationid: mainassociationid minOccurs=0
        @type mainassociationid: string
        @param association: association minOccurs=0 maxOccurs=unbounded
        @type association: RouteTableAssociation
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param routetableid: routetableid minOccurs=0
        @type routetableid: string
        @param route: route minOccurs=0 maxOccurs=unbounded
        @type route: RouteTableRoute
        '''
        RouteTableBase.__init__(self, mainassociationid=mainassociationid, association=association, vpcid=vpcid, routetableid=routetableid, route=route)
