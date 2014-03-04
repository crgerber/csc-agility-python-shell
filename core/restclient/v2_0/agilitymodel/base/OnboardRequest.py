from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class OnboardRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, credential=None, networkPolicy=list(), assetProperties=list(), variables=list(), reboot=None, instance=list(), targetLocation=None, packages=list(), operatingSystem=None, cloud=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credential': {'type': 'Credential', 'name': 'credential', 'native': False}, 'networkPolicy': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networkPolicy', 'minOccurs': '0', 'native': False}, 'assetProperties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'assetProperties', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'reboot': {'type': 'boolean', 'name': 'reboot', 'minOccurs': '0', 'native': True}, 'instance': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'targetLocation': {'type': 'Link', 'name': 'targetLocation', 'native': False}, 'packages': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'packages', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'type': 'string', 'name': 'operatingSystem', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.credential = credential
        self.networkPolicy = networkPolicy
        self.assetProperties = assetProperties
        self.variables = variables
        self.reboot = reboot
        self.instance = instance
        self.targetLocation = targetLocation
        self.packages = packages
        self.operatingSystem = operatingSystem
        self.cloud = cloud 
