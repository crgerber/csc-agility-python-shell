from core.agility.v3_3.agilitymodel.base.ConfigurationPolicyMeta import ConfigurationPolicyMetaBase
from core.agility.v3_3.agilitymodel.actions.ConfigurationPolicyMeta import ConfigurationPolicyMetaActions

class ConfigurationPolicyMeta(ConfigurationPolicyMetaBase, ConfigurationPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, resourcetype=[], designtype=[]):
        '''
        Constructor
        @param resourcetype: resourcetype minOccurs=0 maxOccurs=unbounded
        @type resourcetype: AssetTypeBrief
        @param designtype: designtype minOccurs=0 maxOccurs=unbounded
        @type designtype: AssetTypeBrief
        '''
        ConfigurationPolicyMetaBase.__init__(self, resourcetype=resourcetype, designtype=designtype)
