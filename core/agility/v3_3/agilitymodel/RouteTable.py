from core.agility.v3_3.agilitymodel.base.RouteTable import RouteTableBase
from core.agility.v3_3.agilitymodel.actions.RouteTable import RouteTableActions

class RouteTable(RouteTableBase, RouteTableActions):
    '''
    classdocs
    '''
    def __init__(self, routetableid=None, mainassociationid=None, route=[], association=[], vpcid=None):
        '''
        Constructor
        @param routetableid: routetableid minOccurs=0
        @type routetableid: string
        @param mainassociationid: mainassociationid minOccurs=0
        @type mainassociationid: string
        @param route: route minOccurs=0 maxOccurs=unbounded
        @type route: RouteTableRoute
        @param association: association minOccurs=0 maxOccurs=unbounded
        @type association: RouteTableAssociation
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        '''
        RouteTableBase.__init__(self, routetableid=routetableid, mainassociationid=mainassociationid, route=route, association=association, vpcid=vpcid)
