from core.agility.v3_3.agilitymodel.base.ArtifactType import ArtifactTypeBase
from core.agility.v3_3.agilitymodel.actions.ArtifactType import ArtifactTypeActions

class ArtifactType(ArtifactTypeBase, ArtifactTypeActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], platformservicetype=None):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param platformservicetype: platformservicetype minOccurs=0
        @type platformservicetype: Link
        '''
        ArtifactTypeBase.__init__(self, properties=properties, platformservicetype=platformservicetype)
