from core.agility.v3_3.agilitymodel.base.ConfigurationArtifactType import ConfigurationArtifactTypeBase
from core.agility.v3_3.agilitymodel.actions.ConfigurationArtifactType import ConfigurationArtifactTypeActions

class ConfigurationArtifactType(ConfigurationArtifactTypeBase, ConfigurationArtifactTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        ConfigurationArtifactTypeBase.__init__(self)
