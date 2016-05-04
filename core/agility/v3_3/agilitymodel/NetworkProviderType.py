from base.NetworkProviderType import NetworkProviderTypeBase
from actions.NetworkProviderType import NetworkProviderTypeActions

class NetworkProviderType(NetworkProviderTypeBase, NetworkProviderTypeActions):
    '''
    classdocs
    '''
    def __init__(self, version=None, type=None, properties=[]):
        '''
        Constructor
        @param version: version minOccurs=0
        @type version: string
        @param type: type minOccurs=0
        @type type: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        NetworkProviderTypeBase.__init__(self, version=version, type=type, properties=properties)
