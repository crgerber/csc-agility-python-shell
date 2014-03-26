from core.agility.v2_0.agilitymodel.base.Cloud import CloudBase
from core.agility.v2_0.agilitymodel.actions.Cloud import CloudActions

class Cloud(CloudBase, CloudActions):
    '''
    classdocs
    '''
    def __init__(self, enabled=None, variables=list(), locations=list(), networkServices=list(), cloudCredentials=None, priceEngine=None, networks=list(), postBootScripts=list(), preBootScripts=list(), cloudLogin=None, hostname=None, vmmServer=None, postReleaseScripts=list(), credentials=list(), cloudType=None, proxies=list(), properties=list(), subscription=None, cloudCertificate=None, dhcpOptions=list(), cloudId=None, repositories=list(), vmmPort=None):
        '''
        Constructor
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param networkServices: networkServices minOccurs=0 maxOccurs=unbounded
        @type networkServices: Link
        @param cloudCredentials: cloudCredentials minOccurs=0
        @type cloudCredentials: Credential
        @param priceEngine: priceEngine minOccurs=0
        @type priceEngine: PriceEngine
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param postBootScripts: postBootScripts minOccurs=0 maxOccurs=unbounded
        @type postBootScripts: Link
        @param preBootScripts: preBootScripts minOccurs=0 maxOccurs=unbounded
        @type preBootScripts: Link
        @param cloudLogin: cloudLogin minOccurs=0
        @type cloudLogin: Credential
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param vmmServer: vmmServer minOccurs=0
        @type vmmServer: string
        @param postReleaseScripts: postReleaseScripts minOccurs=0 maxOccurs=unbounded
        @type postReleaseScripts: Link
        @param credentials: credentials minOccurs=0 maxOccurs=unbounded
        @type credentials: Link
        @param cloudType: cloudType minOccurs=0
        @type cloudType: Link
        @param proxies: proxies minOccurs=0 maxOccurs=unbounded
        @type proxies: Proxy
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param subscription: subscription minOccurs=0
        @type subscription: string
        @param cloudCertificate: cloudCertificate minOccurs=0
        @type cloudCertificate: Credential
        @param dhcpOptions: dhcpOptions minOccurs=0 maxOccurs=unbounded
        @type dhcpOptions: Link
        @param cloudId: cloudId minOccurs=0
        @type cloudId: string
        @param repositories: repositories minOccurs=0 maxOccurs=unbounded
        @type repositories: Repository
        @param vmmPort: vmmPort minOccurs=0
        @type vmmPort: int
        '''
        CloudBase.__init__(self, enabled=enabled, variables=variables, locations=locations, networkServices=networkServices, cloudCredentials=cloudCredentials, priceEngine=priceEngine, networks=networks, postBootScripts=postBootScripts, preBootScripts=preBootScripts, cloudLogin=cloudLogin, hostname=hostname, vmmServer=vmmServer, postReleaseScripts=postReleaseScripts, credentials=credentials, cloudType=cloudType, proxies=proxies, properties=properties, subscription=subscription, cloudCertificate=cloudCertificate, dhcpOptions=dhcpOptions, cloudId=cloudId, repositories=repositories, vmmPort=vmmPort)
