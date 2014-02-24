from base.DhcpOptions import DhcpOptionsBase
from actions.DhcpOptions import DhcpOptionsActions

class DhcpOptions(DhcpOptionsBase, DhcpOptionsActions):
    '''
    classdocs
    '''
    def __init__(self, nodeType=None, domainName=None, ntpServers=list(), cloud=None, dsnServers=list(), optionsId=None, properties=list(), netbiosServers=list()):
        '''
        Constructor
        @param nodeType: nodeType minOccurs=0
        @type nodeType: int
        @param domainName: domainName minOccurs=0
        @type domainName: string
        @param ntpServers: ntpServers minOccurs=0 maxOccurs=unbounded
        @type ntpServers: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param dsnServers: dsnServers minOccurs=0 maxOccurs=unbounded
        @type dsnServers: string
        @param optionsId: optionsId minOccurs=0
        @type optionsId: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param netbiosServers: netbiosServers minOccurs=0 maxOccurs=unbounded
        @type netbiosServers: string
        '''
        DhcpOptionsBase.__init__(self, nodeType=nodeType, domainName=domainName, ntpServers=ntpServers, cloud=cloud, dsnServers=dsnServers, optionsId=optionsId, properties=properties, netbiosServers=netbiosServers)
