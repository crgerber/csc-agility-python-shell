from base.ConfigurationArtifact import ConfigurationArtifactBase
from actions.ConfigurationArtifact import ConfigurationArtifactActions

class ConfigurationArtifact(ConfigurationArtifactBase, ConfigurationArtifactActions):
    '''
    classdocs
    '''
    def __init__(self, resource=[], repository=[], documentation=None, version=None, property=[], type=None):
        '''
        Constructor
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: Link
        @param repository: repository minOccurs=0 maxOccurs=unbounded
        @type repository: Link
        @param documentation: documentation minOccurs=0
        @type documentation: string
        @param version: version minOccurs=0
        @type version: string
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: AssetProperty
        @param type: type minOccurs=0
        @type type: string
        '''
        ConfigurationArtifactBase.__init__(self, resource=resource, repository=repository, documentation=documentation, version=version, property=property, type=type)
