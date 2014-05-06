from base.ConfigSettings import ConfigSettingsBase
from actions.ConfigSettings import ConfigSettingsActions

class ConfigSettings(ConfigSettingsBase, ConfigSettingsActions):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        '''
        Constructor
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: Link
        '''
        ConfigSettingsBase.__init__(self, property=property)
