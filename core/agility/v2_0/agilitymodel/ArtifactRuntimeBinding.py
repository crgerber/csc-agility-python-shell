from core.agility.v2_0.agilitymodel.base.ArtifactRuntimeBinding import ArtifactRuntimeBindingBase
from core.agility.v2_0.agilitymodel.actions.ArtifactRuntimeBinding import ArtifactRuntimeBindingActions

class ArtifactRuntimeBinding(ArtifactRuntimeBindingBase, ArtifactRuntimeBindingActions):
    '''
    classdocs
    '''
    def __init__(self, services=list(), runtime=None, type=None, id=None, properties=list()):
        '''
        Constructor
        @param services: services minOccurs=0 maxOccurs=unbounded
        @type services: string
        @param runtime: runtime minOccurs=0
        @type runtime: Link
        @param type: type minOccurs=0
        @type type: Link
        @param id: id
        @type id: int
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ArtifactRuntimeBindingBase.__init__(self, services=services, runtime=runtime, type=type, id=id, properties=properties)
