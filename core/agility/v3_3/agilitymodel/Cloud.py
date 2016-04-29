from core.agility.v3_3.agilitymodel.base.Cloud import CloudBase
from core.agility.v3_3.agilitymodel.actions.Cloud import CloudActions

class Cloud(CloudBase, CloudActions):
    '''
    classdocs
    '''
    def __init__(self, credentials=[], networks=[], dhcpoptions=[], postbootscripts=[], networkservices=[], networksubscriptions=[], postreleasescripts=[], prebootscripts=[], cloudlogin=None, vmmserver=None, hostname=None, vmmport=None, cloudcertificate=None, cloudcredentials=None, properties=[], cloudtype=None, cloudadmincredentials=None, locations=[], repositories=[], priceengine=None, subscription=None, cloudid=None, proxies=[], enabled=None, variables=[], models=[]):
        '''
        Constructor
        @param credentials: credentials minOccurs=0 maxOccurs=unbounded
        @type credentials: Link
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param dhcpoptions: dhcpoptions minOccurs=0 maxOccurs=unbounded
        @type dhcpoptions: Link
        @param postbootscripts: postbootscripts minOccurs=0 maxOccurs=unbounded
        @type postbootscripts: Link
        @param networkservices: networkservices minOccurs=0 maxOccurs=unbounded
        @type networkservices: Link
        @param networksubscriptions: networksubscriptions minOccurs=0 maxOccurs=unbounded
        @type networksubscriptions: NetworkSubscription
        @param postreleasescripts: postreleasescripts minOccurs=0 maxOccurs=unbounded
        @type postreleasescripts: Link
        @param prebootscripts: prebootscripts minOccurs=0 maxOccurs=unbounded
        @type prebootscripts: Link
        @param cloudlogin: cloudlogin minOccurs=0
        @type cloudlogin: Credential
        @param vmmserver: vmmserver minOccurs=0
        @type vmmserver: string
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param vmmport: vmmport minOccurs=0
        @type vmmport: int
        @param cloudcertificate: cloudcertificate minOccurs=0
        @type cloudcertificate: Credential
        @param cloudcredentials: cloudcredentials minOccurs=0
        @type cloudcredentials: Credential
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        @param cloudadmincredentials: cloudadmincredentials minOccurs=0
        @type cloudadmincredentials: Credential
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param repositories: repositories minOccurs=0 maxOccurs=unbounded
        @type repositories: Repository
        @param priceengine: priceengine minOccurs=0
        @type priceengine: PriceEngine
        @param subscription: subscription minOccurs=0
        @type subscription: string
        @param cloudid: cloudid minOccurs=0
        @type cloudid: string
        @param proxies: proxies minOccurs=0 maxOccurs=unbounded
        @type proxies: Proxy
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        '''
        CloudBase.__init__(self, credentials=credentials, networks=networks, dhcpoptions=dhcpoptions, postbootscripts=postbootscripts, networkservices=networkservices, networksubscriptions=networksubscriptions, postreleasescripts=postreleasescripts, prebootscripts=prebootscripts, cloudlogin=cloudlogin, vmmserver=vmmserver, hostname=hostname, vmmport=vmmport, cloudcertificate=cloudcertificate, cloudcredentials=cloudcredentials, properties=properties, cloudtype=cloudtype, cloudadmincredentials=cloudadmincredentials, locations=locations, repositories=repositories, priceengine=priceengine, subscription=subscription, cloudid=cloudid, proxies=proxies, enabled=enabled, variables=variables, models=models)
