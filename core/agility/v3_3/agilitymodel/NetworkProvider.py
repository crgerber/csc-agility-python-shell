from core.agility.v3_3.agilitymodel.base.NetworkProvider import NetworkProviderBase
from core.agility.v3_3.agilitymodel.actions.NetworkProvider import NetworkProviderActions

class NetworkProvider(NetworkProviderBase, NetworkProviderActions):
    '''
    classdocs
    '''
    def __init__(self, networkcredentials=None, defaulttenantid=None, routers=[], hostname=None, networkprovidertype=None, networks=[], floatingips=[]):
        '''
        Constructor
        @param networkcredentials: networkcredentials minOccurs=0
        @type networkcredentials: Credential
        @param defaulttenantid: defaulttenantid minOccurs=0
        @type defaulttenantid: string
        @param routers: routers minOccurs=0 maxOccurs=unbounded
        @type routers: Link
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param networkprovidertype: networkprovidertype minOccurs=0
        @type networkprovidertype: Link
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param floatingips: floatingips minOccurs=0 maxOccurs=unbounded
        @type floatingips: Link
        '''
        NetworkProviderBase.__init__(self, networkcredentials=networkcredentials, defaulttenantid=defaulttenantid, routers=routers, hostname=hostname, networkprovidertype=networkprovidertype, networks=networks, floatingips=floatingips)
