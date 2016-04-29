from core.agility.v3_3.agilitymodel.base.ArtifactRuntimeBinding import ArtifactRuntimeBindingBase
from core.agility.v3_3.agilitymodel.actions.ArtifactRuntimeBinding import ArtifactRuntimeBindingActions

class ArtifactRuntimeBinding(ArtifactRuntimeBindingBase, ArtifactRuntimeBindingActions):
    '''
    classdocs
    '''
    def __init__(self, services=[], properties=[], runtime=None, id=None, type=None):
        '''
        Constructor
        @param services: services minOccurs=0 maxOccurs=unbounded
        @type services: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param runtime: runtime minOccurs=0
        @type runtime: Link
        @param id: id
        @type id: int
        @param type: type minOccurs=0
        @type type: Link
        '''
        ArtifactRuntimeBindingBase.__init__(self, services=services, properties=properties, runtime=runtime, id=id, type=type)
