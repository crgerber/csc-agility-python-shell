from .base.Cloud import CloudBase
from .actions.Cloud import CloudActions

class Cloud(CloudBase, CloudActions):
    '''
    classdocs
    '''
    def __init__(self, enabled=None, variables=[], locations=[], networkservices=[], cloudcredentials=None, priceengine=None, networks=[], postbootscripts=[], prebootscripts=[], cloudlogin=None, hostname=None, vmmserver=None, models=[], postreleasescripts=[], credentials=[], cloudtype=None, proxies=[], properties=[], subscription=None, cloudcertificate=None, dhcpoptions=[], cloudid=None, repositories=[], vmmport=None):
        '''
        Constructor
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param networkservices: networkservices minOccurs=0 maxOccurs=unbounded
        @type networkservices: Link
        @param cloudcredentials: cloudcredentials minOccurs=0
        @type cloudcredentials: Credential
        @param priceengine: priceengine minOccurs=0
        @type priceengine: PriceEngine
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param postbootscripts: postbootscripts minOccurs=0 maxOccurs=unbounded
        @type postbootscripts: Link
        @param prebootscripts: prebootscripts minOccurs=0 maxOccurs=unbounded
        @type prebootscripts: Link
        @param cloudlogin: cloudlogin minOccurs=0
        @type cloudlogin: Credential
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param vmmserver: vmmserver minOccurs=0
        @type vmmserver: string
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        @param postreleasescripts: postreleasescripts minOccurs=0 maxOccurs=unbounded
        @type postreleasescripts: Link
        @param credentials: credentials minOccurs=0 maxOccurs=unbounded
        @type credentials: Link
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        @param proxies: proxies minOccurs=0 maxOccurs=unbounded
        @type proxies: Proxy
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param subscription: subscription minOccurs=0
        @type subscription: string
        @param cloudcertificate: cloudcertificate minOccurs=0
        @type cloudcertificate: Credential
        @param dhcpoptions: dhcpoptions minOccurs=0 maxOccurs=unbounded
        @type dhcpoptions: Link
        @param cloudid: cloudid minOccurs=0
        @type cloudid: string
        @param repositories: repositories minOccurs=0 maxOccurs=unbounded
        @type repositories: Repository
        @param vmmport: vmmport minOccurs=0
        @type vmmport: int
        '''
        CloudBase.__init__(self, enabled=enabled, variables=variables, locations=locations, networkservices=networkservices, cloudcredentials=cloudcredentials, priceengine=priceengine, networks=networks, postbootscripts=postbootscripts, prebootscripts=prebootscripts, cloudlogin=cloudlogin, hostname=hostname, vmmserver=vmmserver, models=models, postreleasescripts=postreleasescripts, credentials=credentials, cloudtype=cloudtype, proxies=proxies, properties=properties, subscription=subscription, cloudcertificate=cloudcertificate, dhcpoptions=dhcpoptions, cloudid=cloudid, repositories=repositories, vmmport=vmmport)
