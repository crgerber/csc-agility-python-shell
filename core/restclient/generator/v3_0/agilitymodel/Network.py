from base.Network import NetworkBase
from actions.Network import NetworkActions

class Network(NetworkBase, NetworkActions):
    '''
    classdocs
    '''
    def __init__(self, networkid=None, networkaddress=None, dnsdomain=None, addressrange=[], locations=[], dsnsearch=[], properties=[], networkgateway=None, networkmask=None, dnsservers=None, cloud=None):
        '''
        Constructor
        @param networkid: networkid minOccurs=0
        @type networkid: string
        @param networkaddress: networkaddress minOccurs=0
        @type networkaddress: string
        @param dnsdomain: dnsdomain minOccurs=0
        @type dnsdomain: string
        @param addressrange: addressrange minOccurs=0 maxOccurs=unbounded
        @type addressrange: Link
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param dsnsearch: dsnsearch minOccurs=0 maxOccurs=unbounded
        @type dsnsearch: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param networkgateway: networkgateway minOccurs=0
        @type networkgateway: string
        @param networkmask: networkmask minOccurs=0
        @type networkmask: string
        @param dnsservers: dnsservers minOccurs=0
        @type dnsservers: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        NetworkBase.__init__(self, networkid=networkid, networkaddress=networkaddress, dnsdomain=dnsdomain, addressrange=addressrange, locations=locations, dsnsearch=dsnsearch, properties=properties, networkgateway=networkgateway, networkmask=networkmask, dnsservers=dnsservers, cloud=cloud)
