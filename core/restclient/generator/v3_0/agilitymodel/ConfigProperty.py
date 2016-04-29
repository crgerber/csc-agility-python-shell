from .base.ConfigProperty import ConfigPropertyBase
from .actions.ConfigProperty import ConfigPropertyActions

class ConfigProperty(ConfigPropertyBase, ConfigPropertyActions):
    '''
    classdocs
    '''
    def __init__(self, value=None):
        '''
        Constructor
        @param value: value minOccurs=0
        @type value: string
        '''
        ConfigPropertyBase.__init__(self, value=value)
