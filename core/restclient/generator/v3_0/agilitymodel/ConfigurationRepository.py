from .base.ConfigurationRepository import ConfigurationRepositoryBase
from .actions.ConfigurationRepository import ConfigurationRepositoryActions

class ConfigurationRepository(ConfigurationRepositoryBase, ConfigurationRepositoryActions):
    '''
    classdocs
    '''
    def __init__(self, repositoryproperty=[], artifactpath=[], repositorytype=None, artifact=[], repositorypath=None, readonly=False, syncintervalseconds=None, artifacttype=None):
        '''
        Constructor
        @param repositoryproperty: repositoryproperty minOccurs=0 maxOccurs=unbounded
        @type repositoryproperty: Property
        @param artifactpath: artifactpath minOccurs=0 maxOccurs=unbounded
        @type artifactpath: string
        @param repositorytype: repositorytype minOccurs=0
        @type repositorytype: string
        @param artifact: artifact minOccurs=0 maxOccurs=unbounded
        @type artifact: Link
        @param repositorypath: repositorypath minOccurs=0
        @type repositorypath: string
        @param readonly: readonly
        @type readonly: boolean
        @param syncintervalseconds: syncintervalseconds minOccurs=0
        @type syncintervalseconds: int
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: string
        '''
        ConfigurationRepositoryBase.__init__(self, repositoryproperty=repositoryproperty, artifactpath=artifactpath, repositorytype=repositorytype, artifact=artifact, repositorypath=repositorypath, readonly=readonly, syncintervalseconds=syncintervalseconds, artifacttype=artifacttype)
