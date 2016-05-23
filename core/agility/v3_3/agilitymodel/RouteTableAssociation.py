from core.agility.v3_3.agilitymodel.base.RouteTableAssociation import RouteTableAssociationBase
from core.agility.v3_3.agilitymodel.actions.RouteTableAssociation import RouteTableAssociationActions

class RouteTableAssociation(RouteTableAssociationBase, RouteTableAssociationActions):
    '''
    classdocs
    '''
    def __init__(self, subnetid=None, associationid=None, main=None, routetableid=None):
        '''
        Constructor
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param associationid: associationid minOccurs=0
        @type associationid: string
        @param main: main minOccurs=0
        @type main: boolean
        @param routetableid: routetableid minOccurs=0
        @type routetableid: string
        '''
        RouteTableAssociationBase.__init__(self, subnetid=subnetid, associationid=associationid, main=main, routetableid=routetableid)
