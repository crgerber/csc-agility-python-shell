from core.agility.v3_3.agilitymodel.base.ConfigRequest import ConfigRequestBase
from core.agility.v3_3.agilitymodel.actions.ConfigRequest import ConfigRequestActions

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
