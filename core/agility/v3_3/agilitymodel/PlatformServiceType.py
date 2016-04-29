from core.agility.v3_3.agilitymodel.base.PlatformServiceType import PlatformServiceTypeBase
from core.agility.v3_3.agilitymodel.actions.PlatformServiceType import PlatformServiceTypeActions

class PlatformServiceType(PlatformServiceTypeBase, PlatformServiceTypeActions):
    '''
    classdocs
    '''
    def __init__(self, servicetypes=[], properties=[], artifacttypes=[], runtimeproperties=[], type=''):
        '''
        Constructor
        @param servicetypes: servicetypes minOccurs=0 maxOccurs=unbounded
        @type servicetypes: ServiceBindingType
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param artifacttypes: artifacttypes minOccurs=0 maxOccurs=unbounded
        @type artifacttypes: ArtifactType
        @param runtimeproperties: runtimeproperties minOccurs=0 maxOccurs=unbounded
        @type runtimeproperties: Property
        @param type: type
        @type type: string
        '''
        PlatformServiceTypeBase.__init__(self, servicetypes=servicetypes, properties=properties, artifacttypes=artifacttypes, runtimeproperties=runtimeproperties, type=type)
