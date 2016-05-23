from core.agility.v3_3.agilitymodel.base.Router import RouterBase
from core.agility.v3_3.agilitymodel.actions.Router import RouterActions

class Router(RouterBase, RouterActions):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, status=None, adminstateup=None, routerid=None, externalnetwork=None, networkprovider=None, routerinterfaces=[]):
        '''
        Constructor
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param status: status minOccurs=0
        @type status: string
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param routerid: routerid minOccurs=0
        @type routerid: string
        @param externalnetwork: externalnetwork minOccurs=0
        @type externalnetwork: Link
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        @param routerinterfaces: routerinterfaces minOccurs=0 maxOccurs=unbounded
        @type routerinterfaces: RouterInterface
        '''
        RouterBase.__init__(self, tenantid=tenantid, status=status, adminstateup=adminstateup, routerid=routerid, externalnetwork=externalnetwork, networkprovider=networkprovider, routerinterfaces=routerinterfaces)
