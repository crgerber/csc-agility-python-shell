from core.agility.common.AgilityModelBase import AgilityModelBase

class OnboardRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, targetlocation=None, operatingsystem=None, instance=[], networkpolicy=[], packages=[], cloud=None, variables=[], mgmtprotocol=None, mgmtport=None, reboot=None, assetproperties=[], credential=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'targetLocation': {'name': 'targetlocation', 'native': False, 'type': 'Link'}, 'operatingSystem': {'name': 'operatingsystem', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'instance': {'name': 'instance', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'networkPolicy': {'name': 'networkpolicy', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'packages': {'name': 'packages', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'mgmtProtocol': {'name': 'mgmtprotocol', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'mgmtPort': {'name': 'mgmtport', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'reboot': {'name': 'reboot', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'assetProperties': {'name': 'assetproperties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'credential': {'name': 'credential', 'native': False, 'type': 'Credential'}})
        self.targetlocation = targetlocation
        self.operatingsystem = operatingsystem
        self.instance = instance
        self.networkpolicy = networkpolicy
        self.packages = packages
        self.cloud = cloud
        self.variables = variables
        self.mgmtprotocol = mgmtprotocol
        self.mgmtport = mgmtport
        self.reboot = reboot
        self.assetproperties = assetproperties
        self.credential = credential 
