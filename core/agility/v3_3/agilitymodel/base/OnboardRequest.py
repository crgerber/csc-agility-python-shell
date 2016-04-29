from core.agility.common.AgilityModelBase import AgilityModelBase

class OnboardRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, reboot=None, credential=None, mgmtport=None, assetproperties=[], instance=[], operatingsystem=None, targetlocation=None, networkpolicy=[], mgmtprotocol=None, cloud=None, packages=[], variables=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credential': {'native': False, 'name': 'credential', 'type': 'Credential'}, 'mgmtPort': {'native': True, 'name': 'mgmtport', 'minOccurs': '0', 'type': 'int'}, 'assetProperties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'assetproperties', 'minOccurs': '0', 'type': 'AssetProperty'}, 'instance': {'maxOccurs': 'unbounded', 'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Link'}, 'operatingSystem': {'native': True, 'name': 'operatingsystem', 'minOccurs': '0', 'type': 'string'}, 'reboot': {'native': True, 'name': 'reboot', 'minOccurs': '0', 'type': 'boolean'}, 'targetLocation': {'native': False, 'name': 'targetlocation', 'type': 'Link'}, 'networkPolicy': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networkpolicy', 'minOccurs': '0', 'type': 'Link'}, 'mgmtProtocol': {'native': True, 'name': 'mgmtprotocol', 'minOccurs': '0', 'type': 'string'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'packages': {'maxOccurs': 'unbounded', 'native': False, 'name': 'packages', 'minOccurs': '0', 'type': 'Link'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.reboot = reboot
        self.credential = credential
        self.mgmtport = mgmtport
        self.assetproperties = assetproperties
        self.instance = instance
        self.operatingsystem = operatingsystem
        self.targetlocation = targetlocation
        self.networkpolicy = networkpolicy
        self.mgmtprotocol = mgmtprotocol
        self.cloud = cloud
        self.packages = packages
        self.variables = variables 
