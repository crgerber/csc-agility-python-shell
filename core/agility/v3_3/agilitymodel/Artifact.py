from core.agility.v3_3.agilitymodel.base.Artifact import ArtifactBase
from core.agility.v3_3.agilitymodel.actions.Artifact import ArtifactActions

class Artifact(ArtifactBase, ArtifactActions):
    '''
    classdocs
    '''
    def __init__(self, buildid=None, configuration=None, builton=None, solution=None, attachments=[]):
        '''
        Constructor
        @param buildid: buildid minOccurs=0
        @type buildid: string
        @param configuration: configuration minOccurs=0
        @type configuration: ArtifactConfiguration
        @param builton: builton minOccurs=0
        @type builton: date
        @param solution: solution minOccurs=0
        @type solution: Link
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        '''
        ArtifactBase.__init__(self, buildid=buildid, configuration=configuration, builton=builton, solution=solution, attachments=attachments)
