from core.agility.v3_3.agilitymodel.base.Router import RouterBase
from core.agility.v3_3.agilitymodel.actions.Router import RouterActions

class Router(RouterBase, RouterActions):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, routerinterfaces=[], networkprovider=None, externalnetwork=None, adminstateup=None, routerid=None, status=None):
        '''
        Constructor
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param routerinterfaces: routerinterfaces minOccurs=0 maxOccurs=unbounded
        @type routerinterfaces: RouterInterface
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        @param externalnetwork: externalnetwork minOccurs=0
        @type externalnetwork: Link
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param routerid: routerid minOccurs=0
        @type routerid: string
        @param status: status minOccurs=0
        @type status: string
        '''
        RouterBase.__init__(self, tenantid=tenantid, routerinterfaces=routerinterfaces, networkprovider=networkprovider, externalnetwork=externalnetwork, adminstateup=adminstateup, routerid=routerid, status=status)
