from core.agility.v3_3.agilitymodel.base.Variable import VariableBase

class ScriptVariableBase(VariableBase):
    '''
    classdocs
    '''
    def __init__(self, overridevalue=None, providersource=None, projectsource=None, variablesource=None, projectvalue=None, environmentsource=None, providervalue=None, topologyvalue=None, package=[], environmentvalue=None, topologysource=None, script=[], providerimagepath=None):
        VariableBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'providerSource': {'name': 'providersource', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'overrideValue': {'name': 'overridevalue', 'minOccurs': '0', 'native': False, 'type': 'Variable'}, 'projectSource': {'name': 'projectsource', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'variableSource': {'name': 'variablesource', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'projectValue': {'name': 'projectvalue', 'minOccurs': '0', 'native': False, 'type': 'Variable'}, 'environmentSource': {'name': 'environmentsource', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'providerValue': {'name': 'providervalue', 'minOccurs': '0', 'native': False, 'type': 'Variable'}, 'topologyValue': {'name': 'topologyvalue', 'minOccurs': '0', 'native': False, 'type': 'Variable'}, 'package': {'name': 'package', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'environmentValue': {'name': 'environmentvalue', 'minOccurs': '0', 'native': False, 'type': 'Variable'}, 'script': {'name': 'script', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'topologySource': {'name': 'topologysource', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'providerImagePath': {'name': 'providerimagepath', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.overridevalue = overridevalue
        self.providersource = providersource
        self.projectsource = projectsource
        self.variablesource = variablesource
        self.projectvalue = projectvalue
        self.environmentsource = environmentsource
        self.providervalue = providervalue
        self.topologyvalue = topologyvalue
        self.package = package
        self.environmentvalue = environmentvalue
        self.topologysource = topologysource
        self.script = script
        self.providerimagepath = providerimagepath 
