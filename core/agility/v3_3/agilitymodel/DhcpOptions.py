from core.agility.v3_3.agilitymodel.base.DhcpOptions import DhcpOptionsBase
from core.agility.v3_3.agilitymodel.actions.DhcpOptions import DhcpOptionsActions

class DhcpOptions(DhcpOptionsBase, DhcpOptionsActions):
    '''
    classdocs
    '''
    def __init__(self, nodetype=None, domainname=None, ntpservers=[], cloud=None, dsnservers=[], optionsid=None, properties=[], netbiosservers=[]):
        '''
        Constructor
        @param nodetype: nodetype minOccurs=0
        @type nodetype: int
        @param domainname: domainname minOccurs=0
        @type domainname: string
        @param ntpservers: ntpservers minOccurs=0 maxOccurs=unbounded
        @type ntpservers: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param dsnservers: dsnservers minOccurs=0 maxOccurs=unbounded
        @type dsnservers: string
        @param optionsid: optionsid minOccurs=0
        @type optionsid: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param netbiosservers: netbiosservers minOccurs=0 maxOccurs=unbounded
        @type netbiosservers: string
        '''
        DhcpOptionsBase.__init__(self, nodetype=nodetype, domainname=domainname, ntpservers=ntpservers, cloud=cloud, dsnservers=dsnservers, optionsid=optionsid, properties=properties, netbiosservers=netbiosservers)
