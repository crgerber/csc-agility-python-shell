from base.RouteTableAssociation import RouteTableAssociationBase
from actions.RouteTableAssociation import RouteTableAssociationActions

class RouteTableAssociation(RouteTableAssociationBase, RouteTableAssociationActions):
    '''
    classdocs
    '''
    def __init__(self, subnetid=None, main=None, routetableid=None, associationid=None):
        '''
        Constructor
        @param subnetid: subnetid minOccurs=0
        @type subnetid: string
        @param main: main minOccurs=0
        @type main: boolean
        @param routetableid: routetableid minOccurs=0
        @type routetableid: string
        @param associationid: associationid minOccurs=0
        @type associationid: string
        '''
        RouteTableAssociationBase.__init__(self, subnetid=subnetid, main=main, routetableid=routetableid, associationid=associationid)
