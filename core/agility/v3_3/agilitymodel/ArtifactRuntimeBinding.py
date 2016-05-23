from core.agility.v3_3.agilitymodel.base.ArtifactRuntimeBinding import ArtifactRuntimeBindingBase
from core.agility.v3_3.agilitymodel.actions.ArtifactRuntimeBinding import ArtifactRuntimeBindingActions

class ArtifactRuntimeBinding(ArtifactRuntimeBindingBase, ArtifactRuntimeBindingActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, services=[], type=None, runtime=None, properties=[]):
        '''
        Constructor
        @param id: id
        @type id: int
        @param services: services minOccurs=0 maxOccurs=unbounded
        @type services: string
        @param type: type minOccurs=0
        @type type: Link
        @param runtime: runtime minOccurs=0
        @type runtime: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ArtifactRuntimeBindingBase.__init__(self, id=id, services=services, type=type, runtime=runtime, properties=properties)
