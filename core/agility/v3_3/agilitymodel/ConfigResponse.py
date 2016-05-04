from base.ConfigResponse import ConfigResponseBase
from actions.ConfigResponse import ConfigResponseActions

class ConfigResponse(ConfigResponseBase, ConfigResponseActions):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        '''
        Constructor
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: Property
        '''
        ConfigResponseBase.__init__(self, property=property)
