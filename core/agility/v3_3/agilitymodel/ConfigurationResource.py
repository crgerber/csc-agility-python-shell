from core.agility.v3_3.agilitymodel.base.ConfigurationResource import ConfigurationResourceBase
from core.agility.v3_3.agilitymodel.actions.ConfigurationResource import ConfigurationResourceActions

class ConfigurationResource(ConfigurationResourceBase, ConfigurationResourceActions):
    '''
    classdocs
    '''
    def __init__(self, variable=[], artifact=None, property=[]):
        '''
        Constructor
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: AssetProperty
        '''
        ConfigurationResourceBase.__init__(self, variable=variable, artifact=artifact, property=property)
