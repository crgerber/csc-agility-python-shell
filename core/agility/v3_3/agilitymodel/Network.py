from core.agility.v3_3.agilitymodel.base.Network import NetworkBase
from core.agility.v3_3.agilitymodel.actions.Network import NetworkActions

class Network(NetworkBase, NetworkActions):
    '''
    classdocs
    '''
    def __init__(self, serviceprovider=[], status=None, networkgateway=None, networkid=None, networkmask=None, dnsdomain=None, tenantid=None, subnets=[], addressrange=[], dnsservers=None, networkaddress=None, dsnsearch=[], routerexternal=None, shared=None, adminstateup=None, networkprovider=None, cloud=None, locations=[], ports=[]):
        '''
        Constructor
        @param serviceprovider: serviceprovider minOccurs=0 maxOccurs=unbounded
        @type serviceprovider: Link
        @param status: status minOccurs=0
        @type status: string
        @param networkgateway: networkgateway minOccurs=0
        @type networkgateway: string
        @param networkid: networkid minOccurs=0
        @type networkid: string
        @param networkmask: networkmask minOccurs=0
        @type networkmask: string
        @param dnsdomain: dnsdomain minOccurs=0
        @type dnsdomain: string
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param subnets: subnets minOccurs=0 maxOccurs=unbounded
        @type subnets: Link
        @param addressrange: addressrange minOccurs=0 maxOccurs=unbounded
        @type addressrange: Link
        @param dnsservers: dnsservers minOccurs=0
        @type dnsservers: string
        @param networkaddress: networkaddress minOccurs=0
        @type networkaddress: string
        @param dsnsearch: dsnsearch minOccurs=0 maxOccurs=unbounded
        @type dsnsearch: string
        @param routerexternal: routerexternal minOccurs=0
        @type routerexternal: boolean
        @param shared: shared minOccurs=0
        @type shared: boolean
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param ports: ports minOccurs=0 maxOccurs=unbounded
        @type ports: Link
        '''
        NetworkBase.__init__(self, serviceprovider=serviceprovider, status=status, networkgateway=networkgateway, networkid=networkid, networkmask=networkmask, dnsdomain=dnsdomain, tenantid=tenantid, subnets=subnets, addressrange=addressrange, dnsservers=dnsservers, networkaddress=networkaddress, dsnsearch=dsnsearch, routerexternal=routerexternal, shared=shared, adminstateup=adminstateup, networkprovider=networkprovider, cloud=cloud, locations=locations, ports=ports)
