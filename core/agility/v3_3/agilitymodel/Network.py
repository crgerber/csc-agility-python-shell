from core.agility.v3_3.agilitymodel.base.Network import NetworkBase
from core.agility.v3_3.agilitymodel.actions.Network import NetworkActions

class Network(NetworkBase, NetworkActions):
    '''
    classdocs
    '''
    def __init__(self, networkid=None, serviceprovider=[], tenantid=None, networkprovider=None, adminstateup=None, routerexternal=None, dnsservers=None, dnsdomain=None, addressrange=[], locations=[], status=None, cloud=None, networkmask=None, networkaddress=None, subnets=[], ports=[], dsnsearch=[], shared=None, networkgateway=None):
        '''
        Constructor
        @param networkid: networkid minOccurs=0
        @type networkid: string
        @param serviceprovider: serviceprovider minOccurs=0 maxOccurs=unbounded
        @type serviceprovider: Link
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param routerexternal: routerexternal minOccurs=0
        @type routerexternal: boolean
        @param dnsservers: dnsservers minOccurs=0
        @type dnsservers: string
        @param dnsdomain: dnsdomain minOccurs=0
        @type dnsdomain: string
        @param addressrange: addressrange minOccurs=0 maxOccurs=unbounded
        @type addressrange: Link
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param status: status minOccurs=0
        @type status: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param networkmask: networkmask minOccurs=0
        @type networkmask: string
        @param networkaddress: networkaddress minOccurs=0
        @type networkaddress: string
        @param subnets: subnets minOccurs=0 maxOccurs=unbounded
        @type subnets: Link
        @param ports: ports minOccurs=0 maxOccurs=unbounded
        @type ports: Link
        @param dsnsearch: dsnsearch minOccurs=0 maxOccurs=unbounded
        @type dsnsearch: string
        @param shared: shared minOccurs=0
        @type shared: boolean
        @param networkgateway: networkgateway minOccurs=0
        @type networkgateway: string
        '''
        NetworkBase.__init__(self, networkid=networkid, serviceprovider=serviceprovider, tenantid=tenantid, networkprovider=networkprovider, adminstateup=adminstateup, routerexternal=routerexternal, dnsservers=dnsservers, dnsdomain=dnsdomain, addressrange=addressrange, locations=locations, status=status, cloud=cloud, networkmask=networkmask, networkaddress=networkaddress, subnets=subnets, ports=ports, dsnsearch=dsnsearch, shared=shared, networkgateway=networkgateway)
