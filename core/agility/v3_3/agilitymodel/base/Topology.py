from core.agility.v3_3.agilitymodel.base.Container import ContainerBase

class TopologyBase(ContainerBase):
    '''
    classdocs
    '''
    def __init__(self, deployer=[], manualstartup=[], mandatoryaffinity=None, accessuriexpanded=None, sourceblueprint=None, launcheraccessuri=[], blueprintsubcontainer=None, antiaffinity=None, resourceaffinity=None, anyorder=[], stats=None, aliases=[], accessuri=None, fixedorder=[], parentproject=None, variables=[]):
        ContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployer': {'maxOccurs': 'unbounded', 'native': False, 'name': 'deployer', 'minOccurs': '0', 'type': 'Link'}, 'manualStartup': {'maxOccurs': 'unbounded', 'native': False, 'name': 'manualstartup', 'minOccurs': '0', 'type': 'Link'}, 'anyOrder': {'maxOccurs': 'unbounded', 'native': False, 'name': 'anyorder', 'minOccurs': '0', 'type': 'Link'}, 'accessUriExpanded': {'native': True, 'name': 'accessuriexpanded', 'minOccurs': '0', 'type': 'string'}, 'sourceBlueprint': {'native': False, 'name': 'sourceblueprint', 'minOccurs': '0', 'type': 'Link'}, 'aliases': {'maxOccurs': 'unbounded', 'native': False, 'name': 'aliases', 'minOccurs': '0', 'type': 'Alias'}, 'blueprintSubcontainer': {'native': True, 'name': 'blueprintsubcontainer', 'minOccurs': '0', 'type': 'boolean'}, 'resourceAffinity': {'native': False, 'name': 'resourceaffinity', 'type': 'ResourceAffinity'}, 'antiAffinity': {'native': True, 'name': 'antiaffinity', 'minOccurs': '0', 'type': 'boolean'}, 'stats': {'native': False, 'name': 'stats', 'minOccurs': '0', 'type': 'TopologyStats'}, 'launcherAccessUri': {'maxOccurs': 'unbounded', 'native': False, 'name': 'launcheraccessuri', 'minOccurs': '0', 'type': 'AccessUri'}, 'mandatoryAffinity': {'native': True, 'name': 'mandatoryaffinity', 'minOccurs': '0', 'type': 'boolean'}, 'accessUri': {'native': True, 'name': 'accessuri', 'minOccurs': '0', 'type': 'string'}, 'parentProject': {'native': False, 'name': 'parentproject', 'minOccurs': '0', 'type': 'Link'}, 'fixedOrder': {'maxOccurs': 'unbounded', 'native': False, 'name': 'fixedorder', 'minOccurs': '0', 'type': 'Link'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.deployer = deployer
        self.manualstartup = manualstartup
        self.mandatoryaffinity = mandatoryaffinity
        self.accessuriexpanded = accessuriexpanded
        self.sourceblueprint = sourceblueprint
        self.launcheraccessuri = launcheraccessuri
        self.blueprintsubcontainer = blueprintsubcontainer
        self.antiaffinity = antiaffinity
        self.resourceaffinity = resourceaffinity
        self.anyorder = anyorder
        self.stats = stats
        self.aliases = aliases
        self.accessuri = accessuri
        self.fixedorder = fixedorder
        self.parentproject = parentproject
        self.variables = variables 
