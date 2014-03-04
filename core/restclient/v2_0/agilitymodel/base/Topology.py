from core.restclient.v2_0.agilitymodel.base.Container import ContainerBase

class TopologyBase(ContainerBase):
    '''
    classdocs
    '''
    def __init__(self, antiAffinity=None, accessUri=None, accessUriExpanded=None, deployer=list(), mandatoryAffinity=None, variables=list(), blueprintSubcontainer=None, manualStartup=list(), resourceAffinity=None, sourceBlueprint=None, fixedOrder=list(), launcherAccessUri=list(), anyOrder=list(), aliases=list()):
        ContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'antiAffinity': {'type': 'boolean', 'name': 'antiAffinity', 'minOccurs': '0', 'native': True}, 'accessUri': {'type': 'string', 'name': 'accessUri', 'minOccurs': '0', 'native': True}, 'accessUriExpanded': {'type': 'string', 'name': 'accessUriExpanded', 'minOccurs': '0', 'native': True}, 'deployer': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'deployer', 'minOccurs': '0', 'native': False}, 'fixedOrder': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'fixedOrder', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'blueprintSubcontainer': {'type': 'boolean', 'name': 'blueprintSubcontainer', 'minOccurs': '0', 'native': True}, 'manualStartup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'manualStartup', 'minOccurs': '0', 'native': False}, 'resourceAffinity': {'type': 'ResourceAffinity', 'name': 'resourceAffinity', 'native': False}, 'aliases': {'maxOccurs': 'unbounded', 'type': 'Alias', 'name': 'aliases', 'minOccurs': '0', 'native': False}, 'mandatoryAffinity': {'type': 'boolean', 'name': 'mandatoryAffinity', 'minOccurs': '0', 'native': True}, 'launcherAccessUri': {'maxOccurs': 'unbounded', 'type': 'AccessUri', 'name': 'launcherAccessUri', 'minOccurs': '0', 'native': False}, 'anyOrder': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'anyOrder', 'minOccurs': '0', 'native': False}, 'sourceBlueprint': {'type': 'Link', 'name': 'sourceBlueprint', 'minOccurs': '0', 'native': False}})
        self.antiAffinity = antiAffinity
        self.accessUri = accessUri
        self.accessUriExpanded = accessUriExpanded
        self.deployer = deployer
        self.mandatoryAffinity = mandatoryAffinity
        self.variables = variables
        self.blueprintSubcontainer = blueprintSubcontainer
        self.manualStartup = manualStartup
        self.resourceAffinity = resourceAffinity
        self.sourceBlueprint = sourceBlueprint
        self.fixedOrder = fixedOrder
        self.launcherAccessUri = launcherAccessUri
        self.anyOrder = anyOrder
        self.aliases = aliases 
