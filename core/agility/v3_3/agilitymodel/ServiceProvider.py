from core.agility.v3_3.agilitymodel.base.ServiceProvider import ServiceProviderBase
from core.agility.v3_3.agilitymodel.actions.ServiceProvider import ServiceProviderActions

class ServiceProvider(ServiceProviderBase, ServiceProviderActions):
    '''
    classdocs
    '''
    def __init__(self, hostname=None, locations=[], properties=[], credentials=None, type=None, networks=[], cloud=None):
        '''
        Constructor
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param type: type minOccurs=0
        @type type: Link
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        ServiceProviderBase.__init__(self, hostname=hostname, locations=locations, properties=properties, credentials=credentials, type=type, networks=networks, cloud=cloud)
