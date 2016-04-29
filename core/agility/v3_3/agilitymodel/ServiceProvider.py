from core.agility.v3_3.agilitymodel.base.ServiceProvider import ServiceProviderBase
from core.agility.v3_3.agilitymodel.actions.ServiceProvider import ServiceProviderActions

class ServiceProvider(ServiceProviderBase, ServiceProviderActions):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, networks=[], properties=[], type=None, cloud=None, hostname=None, locations=[]):
        '''
        Constructor
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        @param type: type minOccurs=0
        @type type: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        '''
        ServiceProviderBase.__init__(self, credentials=credentials, networks=networks, properties=properties, type=type, cloud=cloud, hostname=hostname, locations=locations)
