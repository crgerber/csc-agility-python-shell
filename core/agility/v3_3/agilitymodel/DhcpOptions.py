from core.agility.v3_3.agilitymodel.base.DhcpOptions import DhcpOptionsBase
from core.agility.v3_3.agilitymodel.actions.DhcpOptions import DhcpOptionsActions

class DhcpOptions(DhcpOptionsBase, DhcpOptionsActions):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, dsnservers=[], netbiosservers=[], domainname=None, properties=[], ntpservers=[], nodetype=None, optionsid=None):
        '''
        Constructor
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param dsnservers: dsnservers minOccurs=0 maxOccurs=unbounded
        @type dsnservers: string
        @param netbiosservers: netbiosservers minOccurs=0 maxOccurs=unbounded
        @type netbiosservers: string
        @param domainname: domainname minOccurs=0
        @type domainname: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param ntpservers: ntpservers minOccurs=0 maxOccurs=unbounded
        @type ntpservers: string
        @param nodetype: nodetype minOccurs=0
        @type nodetype: int
        @param optionsid: optionsid minOccurs=0
        @type optionsid: string
        '''
        DhcpOptionsBase.__init__(self, cloud=cloud, dsnservers=dsnservers, netbiosservers=netbiosservers, domainname=domainname, properties=properties, ntpservers=ntpservers, nodetype=nodetype, optionsid=optionsid)
