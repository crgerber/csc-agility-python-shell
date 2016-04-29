from core.agility.v3_3.agilitymodel.base.NetworkProvider import NetworkProviderBase
from core.agility.v3_3.agilitymodel.actions.NetworkProvider import NetworkProviderActions

class NetworkProvider(NetworkProviderBase, NetworkProviderActions):
    '''
    classdocs
    '''
    def __init__(self, routers=[], networks=[], floatingips=[], networkprovidertype=None, networkcredentials=None, defaulttenantid=None, hostname=None):
        '''
        Constructor
        @param routers: routers minOccurs=0 maxOccurs=unbounded
        @type routers: Link
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param floatingips: floatingips minOccurs=0 maxOccurs=unbounded
        @type floatingips: Link
        @param networkprovidertype: networkprovidertype minOccurs=0
        @type networkprovidertype: Link
        @param networkcredentials: networkcredentials minOccurs=0
        @type networkcredentials: Credential
        @param defaulttenantid: defaulttenantid minOccurs=0
        @type defaulttenantid: string
        @param hostname: hostname minOccurs=0
        @type hostname: string
        '''
        NetworkProviderBase.__init__(self, routers=routers, networks=networks, floatingips=floatingips, networkprovidertype=networkprovidertype, networkcredentials=networkcredentials, defaulttenantid=defaulttenantid, hostname=hostname)
