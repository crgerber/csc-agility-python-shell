from base.ConfigurationPolicyMeta import ConfigurationPolicyMetaBase
from actions.ConfigurationPolicyMeta import ConfigurationPolicyMetaActions

class ConfigurationPolicyMeta(ConfigurationPolicyMetaBase, ConfigurationPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, designType=list(), resourceType=list()):
        '''
        Constructor
        @param designType: designType minOccurs=0 maxOccurs=unbounded
        @type designType: AssetTypeBrief
        @param resourceType: resourceType minOccurs=0 maxOccurs=unbounded
        @type resourceType: AssetTypeBrief
        '''
        ConfigurationPolicyMetaBase.__init__(self, designType=designType, resourceType=resourceType)
