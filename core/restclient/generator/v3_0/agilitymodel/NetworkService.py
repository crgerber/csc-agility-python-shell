from .base.NetworkService import NetworkServiceBase
from .actions.NetworkService import NetworkServiceActions

class NetworkService(NetworkServiceBase, NetworkServiceActions):
    '''
    classdocs
    '''
    def __init__(self, hostname=None, networks=[], credentials=None, type=None, properties=[], cloud=None):
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
