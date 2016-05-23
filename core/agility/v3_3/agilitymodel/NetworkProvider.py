from core.agility.v3_3.agilitymodel.base.NetworkProvider import NetworkProviderBase
from core.agility.v3_3.agilitymodel.actions.NetworkProvider import NetworkProviderActions

class NetworkProvider(NetworkProviderBase, NetworkProviderActions):
    '''
    classdocs
    '''
    def __init__(self, networkprovidertype=None, floatingips=[], defaulttenantid=None, routers=[], hostname=None, networks=[], networkcredentials=None):
        '''
        Constructor
        @param networkprovidertype: networkprovidertype minOccurs=0
        @type networkprovidertype: Link
        @param floatingips: floatingips minOccurs=0 maxOccurs=unbounded
        @type floatingips: Link
        @param defaulttenantid: defaulttenantid minOccurs=0
        @type defaulttenantid: string
        @param routers: routers minOccurs=0 maxOccurs=unbounded
        @type routers: Link
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param networkcredentials: networkcredentials minOccurs=0
        @type networkcredentials: Credential
        '''
        NetworkProviderBase.__init__(self, networkprovidertype=networkprovidertype, floatingips=floatingips, defaulttenantid=defaulttenantid, routers=routers, hostname=hostname, networks=networks, networkcredentials=networkcredentials)
