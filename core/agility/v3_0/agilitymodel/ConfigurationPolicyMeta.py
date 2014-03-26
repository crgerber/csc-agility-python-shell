from core.agility.v3_0.agilitymodel.base.ConfigurationPolicyMeta import ConfigurationPolicyMetaBase
from core.agility.v3_0.agilitymodel.actions.ConfigurationPolicyMeta import ConfigurationPolicyMetaActions

class ConfigurationPolicyMeta(ConfigurationPolicyMetaBase, ConfigurationPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, designtype=[], resourcetype=[]):
        '''
        Constructor
        @param designtype: designtype minOccurs=0 maxOccurs=unbounded
        @type designtype: AssetTypeBrief
        @param resourcetype: resourcetype minOccurs=0 maxOccurs=unbounded
        @type resourcetype: AssetTypeBrief
        '''
        ConfigurationPolicyMetaBase.__init__(self, designtype=designtype, resourcetype=resourcetype)
