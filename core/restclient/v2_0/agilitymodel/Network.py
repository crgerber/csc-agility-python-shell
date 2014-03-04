from core.restclient.v2_0.agilitymodel.base.Network import NetworkBase
from core.restclient.v2_0.agilitymodel.actions.Network import NetworkActions

class Network(NetworkBase, NetworkActions):
    '''
    classdocs
    '''
    def __init__(self, networkId=None, networkAddress=None, dnsDomain=None, addressRange=list(), locations=list(), dsnSearch=list(), properties=list(), networkGateway=None, networkMask=None, dnsServers=None, cloud=None):
        '''
        Constructor
        @param networkId: networkId minOccurs=0
        @type networkId: string
        @param networkAddress: networkAddress minOccurs=0
        @type networkAddress: string
        @param dnsDomain: dnsDomain minOccurs=0
        @type dnsDomain: string
        @param addressRange: addressRange minOccurs=0 maxOccurs=unbounded
        @type addressRange: Link
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param dsnSearch: dsnSearch minOccurs=0 maxOccurs=unbounded
        @type dsnSearch: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param networkGateway: networkGateway minOccurs=0
        @type networkGateway: string
        @param networkMask: networkMask minOccurs=0
        @type networkMask: string
        @param dnsServers: dnsServers minOccurs=0
        @type dnsServers: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        NetworkBase.__init__(self, networkId=networkId, networkAddress=networkAddress, dnsDomain=dnsDomain, addressRange=addressRange, locations=locations, dsnSearch=dsnSearch, properties=properties, networkGateway=networkGateway, networkMask=networkMask, dnsServers=dnsServers, cloud=cloud)
