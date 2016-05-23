from core.agility.v3_3.agilitymodel.base.PlatformServiceType import PlatformServiceTypeBase
from core.agility.v3_3.agilitymodel.actions.PlatformServiceType import PlatformServiceTypeActions

class PlatformServiceType(PlatformServiceTypeBase, PlatformServiceTypeActions):
    '''
    classdocs
    '''
    def __init__(self, runtimeproperties=[], servicetypes=[], properties=[], type='', artifacttypes=[]):
        '''
        Constructor
        @param runtimeproperties: runtimeproperties minOccurs=0 maxOccurs=unbounded
        @type runtimeproperties: Property
        @param servicetypes: servicetypes minOccurs=0 maxOccurs=unbounded
        @type servicetypes: ServiceBindingType
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param type: type
        @type type: string
        @param artifacttypes: artifacttypes minOccurs=0 maxOccurs=unbounded
        @type artifacttypes: ArtifactType
        '''
        PlatformServiceTypeBase.__init__(self, runtimeproperties=runtimeproperties, servicetypes=servicetypes, properties=properties, type=type, artifacttypes=artifacttypes)
