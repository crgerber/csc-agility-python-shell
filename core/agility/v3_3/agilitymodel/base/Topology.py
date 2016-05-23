from core.agility.v3_3.agilitymodel.base.Container import ContainerBase

class TopologyBase(ContainerBase):
    '''
    classdocs
    '''
    def __init__(self, launcheraccessuri=[], accessuri=None, parentproject=None, fixedorder=[], anyorder=[], antiaffinity=None, mandatoryaffinity=None, stats=None, sourceblueprint=None, accessuriexpanded=None, blueprintsubcontainer=None, manualstartup=[], variables=[], resourceaffinity=None, aliases=[], deployer=[]):
        ContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'launcherAccessUri': {'name': 'launcheraccessuri', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessUri'}, 'accessUri': {'name': 'accessuri', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'parentProject': {'name': 'parentproject', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'fixedOrder': {'name': 'fixedorder', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'anyOrder': {'name': 'anyorder', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'blueprintSubcontainer': {'name': 'blueprintsubcontainer', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'mandatoryAffinity': {'name': 'mandatoryaffinity', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'stats': {'name': 'stats', 'minOccurs': '0', 'native': False, 'type': 'TopologyStats'}, 'sourceBlueprint': {'name': 'sourceblueprint', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'accessUriExpanded': {'name': 'accessuriexpanded', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'antiAffinity': {'name': 'antiaffinity', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'manualStartup': {'name': 'manualstartup', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'resourceAffinity': {'name': 'resourceaffinity', 'native': False, 'type': 'ResourceAffinity'}, 'aliases': {'name': 'aliases', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Alias'}, 'deployer': {'name': 'deployer', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.launcheraccessuri = launcheraccessuri
        self.accessuri = accessuri
        self.parentproject = parentproject
        self.fixedorder = fixedorder
        self.anyorder = anyorder
        self.antiaffinity = antiaffinity
        self.mandatoryaffinity = mandatoryaffinity
        self.stats = stats
        self.sourceblueprint = sourceblueprint
        self.accessuriexpanded = accessuriexpanded
        self.blueprintsubcontainer = blueprintsubcontainer
        self.manualstartup = manualstartup
        self.variables = variables
        self.resourceaffinity = resourceaffinity
        self.aliases = aliases
        self.deployer = deployer 
