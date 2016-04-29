from .base.ArtifactType import ArtifactTypeBase
from .actions.ArtifactType import ArtifactTypeActions

class ArtifactType(ArtifactTypeBase, ArtifactTypeActions):
    '''
    classdocs
    '''
    def __init__(self, platformservicetype=None, properties=[]):
        '''
        Constructor
        @param platformservicetype: platformservicetype minOccurs=0
        @type platformservicetype: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ArtifactTypeBase.__init__(self, platformservicetype=platformservicetype, properties=properties)
