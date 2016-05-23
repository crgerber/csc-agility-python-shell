from core.agility.v3_3.agilitymodel.base.NetworkProviderType import NetworkProviderTypeBase
from core.agility.v3_3.agilitymodel.actions.NetworkProviderType import NetworkProviderTypeActions

class NetworkProviderType(NetworkProviderTypeBase, NetworkProviderTypeActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], type=None, version=None):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param type: type minOccurs=0
        @type type: string
        @param version: version minOccurs=0
        @type version: string
        '''
        NetworkProviderTypeBase.__init__(self, properties=properties, type=type, version=version)
