from core.agility.v3_0.agilitymodel.base.Variable import VariableBase

class ScriptVariableBase(VariableBase):
    '''
    classdocs
    '''
    def __init__(self, projectvalue=None, topologyvalue=None, projectsource=None, topologysource=None, script=[], variablesource=None, providerimagepath=None, package=[], providersource=None, environmentsource=None, overridevalue=None, environmentvalue=None, providervalue=None):
        VariableBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'projectValue': {'type': 'Variable', 'name': 'projectvalue', 'minOccurs': '0', 'native': False}, 'topologyValue': {'type': 'Variable', 'name': 'topologyvalue', 'minOccurs': '0', 'native': False}, 'projectSource': {'type': 'string', 'name': 'projectsource', 'minOccurs': '0', 'native': True}, 'topologySource': {'type': 'string', 'name': 'topologysource', 'minOccurs': '0', 'native': True}, 'script': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'script', 'minOccurs': '0', 'native': False}, 'variableSource': {'type': 'string', 'name': 'variablesource', 'minOccurs': '0', 'native': True}, 'providerImagePath': {'type': 'string', 'name': 'providerimagepath', 'minOccurs': '0', 'native': True}, 'package': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'package', 'minOccurs': '0', 'native': False}, 'providerSource': {'type': 'string', 'name': 'providersource', 'minOccurs': '0', 'native': True}, 'environmentSource': {'type': 'string', 'name': 'environmentsource', 'minOccurs': '0', 'native': True}, 'overrideValue': {'type': 'Variable', 'name': 'overridevalue', 'minOccurs': '0', 'native': False}, 'environmentValue': {'type': 'Variable', 'name': 'environmentvalue', 'minOccurs': '0', 'native': False}, 'providerValue': {'type': 'Variable', 'name': 'providervalue', 'minOccurs': '0', 'native': False}})
        self.projectvalue = projectvalue
        self.topologyvalue = topologyvalue
        self.projectsource = projectsource
        self.topologysource = topologysource
        self.script = script
        self.variablesource = variablesource
        self.providerimagepath = providerimagepath
        self.package = package
        self.providersource = providersource
        self.environmentsource = environmentsource
        self.overridevalue = overridevalue
        self.environmentvalue = environmentvalue
        self.providervalue = providervalue 
