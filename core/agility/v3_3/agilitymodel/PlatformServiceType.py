from core.agility.v3_3.agilitymodel.base.PlatformServiceType import PlatformServiceTypeBase
from core.agility.v3_3.agilitymodel.actions.PlatformServiceType import PlatformServiceTypeActions

class PlatformServiceType(PlatformServiceTypeBase, PlatformServiceTypeActions):
    '''
    classdocs
    '''
    def __init__(self, artifacttypes=[], runtimeproperties=[], servicetypes=[], type='', properties=[]):
        '''
        Constructor
        @param artifacttypes: artifacttypes minOccurs=0 maxOccurs=unbounded
        @type artifacttypes: ArtifactType
        @param runtimeproperties: runtimeproperties minOccurs=0 maxOccurs=unbounded
        @type runtimeproperties: Property
        @param servicetypes: servicetypes minOccurs=0 maxOccurs=unbounded
        @type servicetypes: ServiceBindingType
        @param type: type
        @type type: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        PlatformServiceTypeBase.__init__(self, artifacttypes=artifacttypes, runtimeproperties=runtimeproperties, servicetypes=servicetypes, type=type, properties=properties)
