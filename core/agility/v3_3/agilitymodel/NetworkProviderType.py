from core.agility.v3_3.agilitymodel.base.NetworkProviderType import NetworkProviderTypeBase
from core.agility.v3_3.agilitymodel.actions.NetworkProviderType import NetworkProviderTypeActions

class NetworkProviderType(NetworkProviderTypeBase, NetworkProviderTypeActions):
    '''
    classdocs
    '''
    def __init__(self, version=None, properties=[], type=None):
        '''
        Constructor
        @param version: version minOccurs=0
        @type version: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param type: type minOccurs=0
        @type type: string
        '''
        NetworkProviderTypeBase.__init__(self, version=version, properties=properties, type=type)
