from core.agility.v3_3.agilitymodel.base.ConfigurationRepository import ConfigurationRepositoryBase
from core.agility.v3_3.agilitymodel.actions.ConfigurationRepository import ConfigurationRepositoryActions

class ConfigurationRepository(ConfigurationRepositoryBase, ConfigurationRepositoryActions):
    '''
    classdocs
    '''
    def __init__(self, repositorypath=None, artifact=[], repositorytype=None, readonly=False, repositoryproperty=[], artifacttype=None, artifactpath=[], syncintervalseconds=None):
        '''
        Constructor
        @param repositorypath: repositorypath minOccurs=0
        @type repositorypath: string
        @param artifact: artifact minOccurs=0 maxOccurs=unbounded
        @type artifact: Link
        @param repositorytype: repositorytype minOccurs=0
        @type repositorytype: string
        @param readonly: readonly
        @type readonly: boolean
        @param repositoryproperty: repositoryproperty minOccurs=0 maxOccurs=unbounded
        @type repositoryproperty: Property
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: string
        @param artifactpath: artifactpath minOccurs=0 maxOccurs=unbounded
        @type artifactpath: string
        @param syncintervalseconds: syncintervalseconds minOccurs=0
        @type syncintervalseconds: int
        '''
        ConfigurationRepositoryBase.__init__(self, repositorypath=repositorypath, artifact=artifact, repositorytype=repositorytype, readonly=readonly, repositoryproperty=repositoryproperty, artifacttype=artifacttype, artifactpath=artifactpath, syncintervalseconds=syncintervalseconds)
