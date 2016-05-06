from core.agility.v3_3.agilitymodel.base.ConfigResponse import ConfigResponseBase
from core.agility.v3_3.agilitymodel.actions.ConfigResponse import ConfigResponseActions

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
