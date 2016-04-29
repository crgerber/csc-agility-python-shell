from core.agility.v3_3.agilitymodel.base.Artifact import ArtifactBase
from core.agility.v3_3.agilitymodel.actions.Artifact import ArtifactActions

class Artifact(ArtifactBase, ArtifactActions):
    '''
    classdocs
    '''
    def __init__(self, configuration=None, buildid=None, solution=None, attachments=[], builton=None):
        '''
        Constructor
        @param configuration: configuration minOccurs=0
        @type configuration: ArtifactConfiguration
        @param buildid: buildid minOccurs=0
        @type buildid: string
        @param solution: solution minOccurs=0
        @type solution: Link
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        @param builton: builton minOccurs=0
        @type builton: date
        '''
        ArtifactBase.__init__(self, configuration=configuration, buildid=buildid, solution=solution, attachments=attachments, builton=builton)
