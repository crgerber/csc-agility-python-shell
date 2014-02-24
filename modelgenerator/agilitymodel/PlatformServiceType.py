from base.PlatformServiceType import PlatformServiceTypeBase
from actions.PlatformServiceType import PlatformServiceTypeActions

class PlatformServiceType(PlatformServiceTypeBase, PlatformServiceTypeActions):
    '''
    classdocs
    '''
    def __init__(self, artifactTypes=list(), runtimeProperties=list(), serviceTypes=list(), type='', properties=list()):
        '''
        Constructor
        @param artifactTypes: artifactTypes minOccurs=0 maxOccurs=unbounded
        @type artifactTypes: ArtifactType
        @param runtimeProperties: runtimeProperties minOccurs=0 maxOccurs=unbounded
        @type runtimeProperties: Property
        @param serviceTypes: serviceTypes minOccurs=0 maxOccurs=unbounded
        @type serviceTypes: ServiceBindingType
        @param type: type
        @type type: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        PlatformServiceTypeBase.__init__(self, artifactTypes=artifactTypes, runtimeProperties=runtimeProperties, serviceTypes=serviceTypes, type=type, properties=properties)
