from core.agility.v3_3.agilitymodel.base.Artifact import ArtifactBase
from core.agility.v3_3.agilitymodel.actions.Artifact import ArtifactActions

class Artifact(ArtifactBase, ArtifactActions):
    '''
    classdocs
    '''
    def __init__(self, configuration=None, builton=None, buildid=None, attachments=[], solution=None):
        '''
        Constructor
        @param configuration: configuration minOccurs=0
        @type configuration: ArtifactConfiguration
        @param builton: builton minOccurs=0
        @type builton: date
        @param buildid: buildid minOccurs=0
        @type buildid: string
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        @param solution: solution minOccurs=0
        @type solution: Link
        '''
        ArtifactBase.__init__(self, configuration=configuration, builton=builton, buildid=buildid, attachments=attachments, solution=solution)
