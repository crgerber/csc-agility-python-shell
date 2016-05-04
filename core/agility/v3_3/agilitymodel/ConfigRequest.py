from base.ConfigRequest import ConfigRequestBase
from actions.ConfigRequest import ConfigRequestActions

class ConfigRequest(ConfigRequestBase, ConfigRequestActions):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        '''
        Constructor
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: string
        '''
        ConfigRequestBase.__init__(self, property=property)
