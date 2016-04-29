from core.agility.v3_3.agilitymodel.base.RouteTableAssociation import RouteTableAssociationBase
from core.agility.v3_3.agilitymodel.actions.RouteTableAssociation import RouteTableAssociationActions

class RouteTableAssociation(RouteTableAssociationBase, RouteTableAssociationActions):
    '''
    classdocs
    '''
    def __init__(self, routetableid=None, subnetid=None, associationid=None, main=None):
        '''
        Constructor
        @param routetableid: routetableid minOccurs=0
        @type routetableid: string
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param associationid: associationid minOccurs=0
        @type associationid: string
        @param main: main minOccurs=0
        @type main: boolean
        '''
        RouteTableAssociationBase.__init__(self, routetableid=routetableid, subnetid=subnetid, associationid=associationid, main=main)
