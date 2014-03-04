from core.restclient.v2_0.agilitymodel.base.ConfigSettings import ConfigSettingsBase
from core.restclient.v2_0.agilitymodel.actions.ConfigSettings import ConfigSettingsActions

class ConfigSettings(ConfigSettingsBase, ConfigSettingsActions):
    '''
    classdocs
    '''
    def __init__(self, property=list()):
        '''
        Constructor
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: Link
        '''
        ConfigSettingsBase.__init__(self, property=property)
