from core.agility.v3_3.agilitymodel.base.Variable import VariableBase

class ScriptVariableBase(VariableBase):
    '''
    classdocs
    '''
    def __init__(self, topologysource=None, projectsource=None, package=[], projectvalue=None, script=[], providervalue=None, providersource=None, overridevalue=None, providerimagepath=None, variablesource=None, environmentvalue=None, environmentsource=None, topologyvalue=None):
        VariableBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'topologySource': {'native': True, 'name': 'topologysource', 'minOccurs': '0', 'type': 'string'}, 'projectSource': {'native': True, 'name': 'projectsource', 'minOccurs': '0', 'type': 'string'}, 'package': {'maxOccurs': 'unbounded', 'native': False, 'name': 'package', 'minOccurs': '0', 'type': 'Link'}, 'projectValue': {'native': False, 'name': 'projectvalue', 'minOccurs': '0', 'type': 'Variable'}, 'script': {'maxOccurs': 'unbounded', 'native': False, 'name': 'script', 'minOccurs': '0', 'type': 'Link'}, 'providerValue': {'native': False, 'name': 'providervalue', 'minOccurs': '0', 'type': 'Variable'}, 'providerSource': {'native': True, 'name': 'providersource', 'minOccurs': '0', 'type': 'string'}, 'overrideValue': {'native': False, 'name': 'overridevalue', 'minOccurs': '0', 'type': 'Variable'}, 'providerImagePath': {'native': True, 'name': 'providerimagepath', 'minOccurs': '0', 'type': 'string'}, 'variableSource': {'native': True, 'name': 'variablesource', 'minOccurs': '0', 'type': 'string'}, 'environmentValue': {'native': False, 'name': 'environmentvalue', 'minOccurs': '0', 'type': 'Variable'}, 'environmentSource': {'native': True, 'name': 'environmentsource', 'minOccurs': '0', 'type': 'string'}, 'topologyValue': {'native': False, 'name': 'topologyvalue', 'minOccurs': '0', 'type': 'Variable'}})
        self.topologysource = topologysource
        self.projectsource = projectsource
        self.package = package
        self.projectvalue = projectvalue
        self.script = script
        self.providervalue = providervalue
        self.providersource = providersource
        self.overridevalue = overridevalue
        self.providerimagepath = providerimagepath
        self.variablesource = variablesource
        self.environmentvalue = environmentvalue
        self.environmentsource = environmentsource
        self.topologyvalue = topologyvalue 
