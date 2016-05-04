from base.Network import NetworkBase
from actions.Network import NetworkActions

class Network(NetworkBase, NetworkActions):
    '''
    classdocs
    '''
    def __init__(self, networkid=None, subnets=[], adminstateup=None, networkaddress=None, dnsdomain=None, serviceprovider=[], addressrange=[], locations=[], dsnsearch=[], tenantid=None, status=None, networkprovider=None, networkgateway=None, shared=None, routerexternal=None, networkmask=None, dnsservers=None, cloud=None, ports=[]):
        '''
        Constructor
        @param networkid: networkid minOccurs=0
        @type networkid: string
        @param subnets: subnets minOccurs=0 maxOccurs=unbounded
        @type subnets: Link
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param networkaddress: networkaddress minOccurs=0
        @type networkaddress: string
        @param dnsdomain: dnsdomain minOccurs=0
        @type dnsdomain: string
        @param serviceprovider: serviceprovider minOccurs=0 maxOccurs=unbounded
        @type serviceprovider: Link
        @param addressrange: addressrange minOccurs=0 maxOccurs=unbounded
        @type addressrange: Link
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param dsnsearch: dsnsearch minOccurs=0 maxOccurs=unbounded
        @type dsnsearch: string
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param status: status minOccurs=0
        @type status: string
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        @param networkgateway: networkgateway minOccurs=0
        @type networkgateway: string
        @param shared: shared minOccurs=0
        @type shared: boolean
        @param routerexternal: routerexternal minOccurs=0
        @type routerexternal: boolean
        @param networkmask: networkmask minOccurs=0
        @type networkmask: string
        @param dnsservers: dnsservers minOccurs=0
        @type dnsservers: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param ports: ports minOccurs=0 maxOccurs=unbounded
        @type ports: Link
        '''
        NetworkBase.__init__(self, networkid=networkid, subnets=subnets, adminstateup=adminstateup, networkaddress=networkaddress, dnsdomain=dnsdomain, serviceprovider=serviceprovider, addressrange=addressrange, locations=locations, dsnsearch=dsnsearch, tenantid=tenantid, status=status, networkprovider=networkprovider, networkgateway=networkgateway, shared=shared, routerexternal=routerexternal, networkmask=networkmask, dnsservers=dnsservers, cloud=cloud, ports=ports)
