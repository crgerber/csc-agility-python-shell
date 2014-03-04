from core.restclient.v2_0.agilitymodel.base.ArtifactType import ArtifactTypeBase
from core.restclient.v2_0.agilitymodel.actions.ArtifactType import ArtifactTypeActions

class ArtifactType(ArtifactTypeBase, ArtifactTypeActions):
    '''
    classdocs
    '''
    def __init__(self, platformServiceType=None, properties=list()):
        '''
        Constructor
        @param platformServiceType: platformServiceType minOccurs=0
        @type platformServiceType: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ArtifactTypeBase.__init__(self, platformServiceType=platformServiceType, properties=properties)
