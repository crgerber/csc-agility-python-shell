from core.agility.v3_3.agilitymodel.base.Cloud import CloudBase
from core.agility.v3_3.agilitymodel.actions.Cloud import CloudActions

class Cloud(CloudBase, CloudActions):
    '''
    classdocs
    '''
    def __init__(self, postreleasescripts=[], hostname=None, postbootscripts=[], vmmserver=None, cloudcredentials=None, cloudcertificate=None, enabled=None, locations=[], credentials=[], networksubscriptions=[], variables=[], priceengine=None, prebootscripts=[], repositories=[], cloudid=None, properties=[], proxies=[], dhcpoptions=[], cloudtype=None, cloudadmincredentials=None, cloudlogin=None, networkservices=[], vmmport=None, subscription=None, networks=[], models=[]):
        '''
        Constructor
        @param postreleasescripts: postreleasescripts minOccurs=0 maxOccurs=unbounded
        @type postreleasescripts: Link
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param postbootscripts: postbootscripts minOccurs=0 maxOccurs=unbounded
        @type postbootscripts: Link
        @param vmmserver: vmmserver minOccurs=0
        @type vmmserver: string
        @param cloudcredentials: cloudcredentials minOccurs=0
        @type cloudcredentials: Credential
        @param cloudcertificate: cloudcertificate minOccurs=0
        @type cloudcertificate: Credential
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: Link
        @param credentials: credentials minOccurs=0 maxOccurs=unbounded
        @type credentials: Link
        @param networksubscriptions: networksubscriptions minOccurs=0 maxOccurs=unbounded
        @type networksubscriptions: NetworkSubscription
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param priceengine: priceengine minOccurs=0
        @type priceengine: PriceEngine
        @param prebootscripts: prebootscripts minOccurs=0 maxOccurs=unbounded
        @type prebootscripts: Link
        @param repositories: repositories minOccurs=0 maxOccurs=unbounded
        @type repositories: Repository
        @param cloudid: cloudid minOccurs=0
        @type cloudid: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param proxies: proxies minOccurs=0 maxOccurs=unbounded
        @type proxies: Proxy
        @param dhcpoptions: dhcpoptions minOccurs=0 maxOccurs=unbounded
        @type dhcpoptions: Link
        @param cloudtype: cloudtype minOccurs=0
        @type cloudtype: Link
        @param cloudadmincredentials: cloudadmincredentials minOccurs=0
        @type cloudadmincredentials: Credential
        @param cloudlogin: cloudlogin minOccurs=0
        @type cloudlogin: Credential
        @param networkservices: networkservices minOccurs=0 maxOccurs=unbounded
        @type networkservices: Link
        @param vmmport: vmmport minOccurs=0
        @type vmmport: int
        @param subscription: subscription minOccurs=0
        @type subscription: string
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        '''
        CloudBase.__init__(self, postreleasescripts=postreleasescripts, hostname=hostname, postbootscripts=postbootscripts, vmmserver=vmmserver, cloudcredentials=cloudcredentials, cloudcertificate=cloudcertificate, enabled=enabled, locations=locations, credentials=credentials, networksubscriptions=networksubscriptions, variables=variables, priceengine=priceengine, prebootscripts=prebootscripts, repositories=repositories, cloudid=cloudid, properties=properties, proxies=proxies, dhcpoptions=dhcpoptions, cloudtype=cloudtype, cloudadmincredentials=cloudadmincredentials, cloudlogin=cloudlogin, networkservices=networkservices, vmmport=vmmport, subscription=subscription, networks=networks, models=models)
