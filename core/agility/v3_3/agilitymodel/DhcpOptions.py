from core.agility.v3_3.agilitymodel.base.DhcpOptions import DhcpOptionsBase
from core.agility.v3_3.agilitymodel.actions.DhcpOptions import DhcpOptionsActions

class DhcpOptions(DhcpOptionsBase, DhcpOptionsActions):
    '''
    classdocs
    '''
    def __init__(self, netbiosservers=[], domainname=None, nodetype=None, properties=[], optionsid=None, cloud=None, dsnservers=[], ntpservers=[]):
        '''
        Constructor
        @param netbiosservers: netbiosservers minOccurs=0 maxOccurs=unbounded
        @type netbiosservers: string
        @param domainname: domainname minOccurs=0
        @type domainname: string
        @param nodetype: nodetype minOccurs=0
        @type nodetype: int
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param optionsid: optionsid minOccurs=0
        @type optionsid: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param dsnservers: dsnservers minOccurs=0 maxOccurs=unbounded
        @type dsnservers: string
        @param ntpservers: ntpservers minOccurs=0 maxOccurs=unbounded
        @type ntpservers: string
        '''
        DhcpOptionsBase.__init__(self, netbiosservers=netbiosservers, domainname=domainname, nodetype=nodetype, properties=properties, optionsid=optionsid, cloud=cloud, dsnservers=dsnservers, ntpservers=ntpservers)
