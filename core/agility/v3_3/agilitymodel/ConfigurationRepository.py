from core.agility.v3_3.agilitymodel.base.ConfigurationRepository import ConfigurationRepositoryBase
from core.agility.v3_3.agilitymodel.actions.ConfigurationRepository import ConfigurationRepositoryActions

class ConfigurationRepository(ConfigurationRepositoryBase, ConfigurationRepositoryActions):
    '''
    classdocs
    '''
    def __init__(self, artifacttype=None, repositoryproperty=[], artifactpath=[], repositorytype=None, readonly=False, artifact=[], syncintervalseconds=None, repositorypath=None):
        '''
        Constructor
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: string
        @param repositoryproperty: repositoryproperty minOccurs=0 maxOccurs=unbounded
        @type repositoryproperty: Property
        @param artifactpath: artifactpath minOccurs=0 maxOccurs=unbounded
        @type artifactpath: string
        @param repositorytype: repositorytype minOccurs=0
        @type repositorytype: string
        @param readonly: readonly
        @type readonly: boolean
        @param artifact: artifact minOccurs=0 maxOccurs=unbounded
        @type artifact: Link
        @param syncintervalseconds: syncintervalseconds minOccurs=0
        @type syncintervalseconds: int
        @param repositorypath: repositorypath minOccurs=0
        @type repositorypath: string
        '''
        ConfigurationRepositoryBase.__init__(self, artifacttype=artifacttype, repositoryproperty=repositoryproperty, artifactpath=artifactpath, repositorytype=repositorytype, readonly=readonly, artifact=artifact, syncintervalseconds=syncintervalseconds, repositorypath=repositorypath)
