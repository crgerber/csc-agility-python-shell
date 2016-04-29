from .Container import ContainerBase

class TopologyBase(ContainerBase):
    '''
    classdocs
    '''
    def __init__(self, antiaffinity=None, accessuri=None, accessuriexpanded=None, deployer=[], mandatoryaffinity=None, variables=[], blueprintsubcontainer=None, manualstartup=[], resourceaffinity=None, sourceblueprint=None, fixedorder=[], launcheraccessuri=[], anyorder=[], aliases=[]):
        ContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'antiAffinity': {'type': 'boolean', 'name': 'antiaffinity', 'minOccurs': '0', 'native': True}, 'accessUri': {'type': 'string', 'name': 'accessuri', 'minOccurs': '0', 'native': True}, 'accessUriExpanded': {'type': 'string', 'name': 'accessuriexpanded', 'minOccurs': '0', 'native': True}, 'deployer': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'deployer', 'minOccurs': '0', 'native': False}, 'fixedOrder': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'fixedorder', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'blueprintSubcontainer': {'type': 'boolean', 'name': 'blueprintsubcontainer', 'minOccurs': '0', 'native': True}, 'manualStartup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'manualstartup', 'minOccurs': '0', 'native': False}, 'resourceAffinity': {'type': 'ResourceAffinity', 'name': 'resourceaffinity', 'native': False}, 'aliases': {'maxOccurs': 'unbounded', 'type': 'Alias', 'name': 'aliases', 'minOccurs': '0', 'native': False}, 'mandatoryAffinity': {'type': 'boolean', 'name': 'mandatoryaffinity', 'minOccurs': '0', 'native': True}, 'launcherAccessUri': {'maxOccurs': 'unbounded', 'type': 'AccessUri', 'name': 'launcheraccessuri', 'minOccurs': '0', 'native': False}, 'anyOrder': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'anyorder', 'minOccurs': '0', 'native': False}, 'sourceBlueprint': {'type': 'Link', 'name': 'sourceblueprint', 'minOccurs': '0', 'native': False}})
        self.antiaffinity = antiaffinity
        self.accessuri = accessuri
        self.accessuriexpanded = accessuriexpanded
        self.deployer = deployer
        self.mandatoryaffinity = mandatoryaffinity
        self.variables = variables
        self.blueprintsubcontainer = blueprintsubcontainer
        self.manualstartup = manualstartup
        self.resourceaffinity = resourceaffinity
        self.sourceblueprint = sourceblueprint
        self.fixedorder = fixedorder
        self.launcheraccessuri = launcheraccessuri
        self.anyorder = anyorder
        self.aliases = aliases 
