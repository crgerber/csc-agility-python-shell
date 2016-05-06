from core.agility.v3_3.agilitymodel.base.ConfigurationResource import ConfigurationResourceBase
from core.agility.v3_3.agilitymodel.actions.ConfigurationResource import ConfigurationResourceActions

class ConfigurationResource(ConfigurationResourceBase, ConfigurationResourceActions):
    '''
    classdocs
    '''
    def __init__(self, variable=[], property=[], artifact=None):
        '''
        Constructor
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: AssetProperty
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        '''
        ConfigurationResourceBase.__init__(self, variable=variable, property=property, artifact=artifact)
