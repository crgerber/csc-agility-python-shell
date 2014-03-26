from core.agility.common.AgilityModelBase import AgilityModelBase


class OnboardRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, credential=None, networkpolicy=[], assetproperties=[], variables=[], reboot=None, instance=[], mgmtport=None, mgmtprotocol=None, targetlocation=None, packages=[], operatingsystem=None, cloud=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credential': {'type': 'Credential', 'name': 'credential', 'native': False}, 'networkPolicy': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networkpolicy', 'minOccurs': '0', 'native': False}, 'assetProperties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'assetproperties', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'reboot': {'type': 'boolean', 'name': 'reboot', 'minOccurs': '0', 'native': True}, 'instance': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'mgmtPort': {'type': 'int', 'name': 'mgmtport', 'minOccurs': '0', 'native': True}, 'mgmtProtocol': {'type': 'string', 'name': 'mgmtprotocol', 'minOccurs': '0', 'native': True}, 'targetLocation': {'type': 'Link', 'name': 'targetlocation', 'native': False}, 'packages': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'packages', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'type': 'string', 'name': 'operatingsystem', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.credential = credential
        self.networkpolicy = networkpolicy
        self.assetproperties = assetproperties
        self.variables = variables
        self.reboot = reboot
        self.instance = instance
        self.mgmtport = mgmtport
        self.mgmtprotocol = mgmtprotocol
        self.targetlocation = targetlocation
        self.packages = packages
        self.operatingsystem = operatingsystem
        self.cloud = cloud 
