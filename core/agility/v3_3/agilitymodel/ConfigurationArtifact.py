from core.agility.v3_3.agilitymodel.base.ConfigurationArtifact import ConfigurationArtifactBase
from core.agility.v3_3.agilitymodel.actions.ConfigurationArtifact import ConfigurationArtifactActions

class ConfigurationArtifact(ConfigurationArtifactBase, ConfigurationArtifactActions):
    '''
    classdocs
    '''
    def __init__(self, property=[], documentation=None, version=None, repository=[], type=None, resource=[]):
        '''
        Constructor
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: AssetProperty
        @param documentation: documentation minOccurs=0
        @type documentation: string
        @param version: version minOccurs=0
        @type version: string
        @param repository: repository minOccurs=0 maxOccurs=unbounded
        @type repository: Link
        @param type: type minOccurs=0
        @type type: string
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: Link
        '''
        ConfigurationArtifactBase.__init__(self, property=property, documentation=documentation, version=version, repository=repository, type=type, resource=resource)
