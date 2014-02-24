from base.Artifact import ArtifactBase
from actions.Artifact import ArtifactActions

class Artifact(ArtifactBase, ArtifactActions):
    '''
    classdocs
    '''
    def __init__(self, buildId=None, configuration=None, builtOn=None, solution=None, attachments=list()):
        '''
        Constructor
        @param buildId: buildId minOccurs=0
        @type buildId: string
        @param configuration: configuration minOccurs=0
        @type configuration: ArtifactConfiguration
        @param builtOn: builtOn minOccurs=0
        @type builtOn: date
        @param solution: solution minOccurs=0
        @type solution: Link
        @param attachments: attachments minOccurs=0 maxOccurs=unbounded
        @type attachments: Link
        '''
        ArtifactBase.__init__(self, buildId=buildId, configuration=configuration, builtOn=builtOn, solution=solution, attachments=attachments)
