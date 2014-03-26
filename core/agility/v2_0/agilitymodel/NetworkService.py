from core.agility.v2_0.agilitymodel.base.NetworkService import NetworkServiceBase
from core.agility.v2_0.agilitymodel.actions.NetworkService import NetworkServiceActions

class NetworkService(NetworkServiceBase, NetworkServiceActions):
    '''
    classdocs
    '''
    def __init__(self, hostname=None, networks=list(), credentials=None, type=None, properties=list(), cloud=None):
        '''
        Constructor
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param type: type minOccurs=0
        @type type: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        NetworkServiceBase.__init__(self, hostname=hostname, networks=networks, credentials=credentials, type=type, properties=properties, cloud=cloud)
