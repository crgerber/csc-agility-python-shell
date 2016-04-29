from .base.ConfigurationArtifactType import ConfigurationArtifactTypeBase
from .actions.ConfigurationArtifactType import ConfigurationArtifactTypeActions

class ConfigurationArtifactType(ConfigurationArtifactTypeBase, ConfigurationArtifactTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        ConfigurationArtifactTypeBase.__init__(self)
