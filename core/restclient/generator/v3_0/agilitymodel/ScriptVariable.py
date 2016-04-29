from .base.ScriptVariable import ScriptVariableBase
from .actions.ScriptVariable import ScriptVariableActions

class ScriptVariable(ScriptVariableBase, ScriptVariableActions):
    '''
    classdocs
    '''
    def __init__(self, projectvalue=None, topologyvalue=None, projectsource=None, topologysource=None, script=[], variablesource=None, providerimagepath=None, package=[], providersource=None, environmentsource=None, overridevalue=None, environmentvalue=None, providervalue=None):
        '''
        Constructor
        @param projectvalue: projectvalue minOccurs=0
        @type projectvalue: Variable
        @param topologyvalue: topologyvalue minOccurs=0
        @type topologyvalue: Variable
        @param projectsource: projectsource minOccurs=0
        @type projectsource: string
        @param topologysource: topologysource minOccurs=0
        @type topologysource: string
        @param script: script minOccurs=0 maxOccurs=unbounded
        @type script: Link
        @param variablesource: variablesource minOccurs=0
        @type variablesource: string
        @param providerimagepath: providerimagepath minOccurs=0
        @type providerimagepath: string
        @param package: package minOccurs=0 maxOccurs=unbounded
        @type package: Link
        @param providersource: providersource minOccurs=0
        @type providersource: string
        @param environmentsource: environmentsource minOccurs=0
        @type environmentsource: string
        @param overridevalue: overridevalue minOccurs=0
        @type overridevalue: Variable
        @param environmentvalue: environmentvalue minOccurs=0
        @type environmentvalue: Variable
        @param providervalue: providervalue minOccurs=0
        @type providervalue: Variable
        '''
        ScriptVariableBase.__init__(self, projectvalue=projectvalue, topologyvalue=topologyvalue, projectsource=projectsource, topologysource=topologysource, script=script, variablesource=variablesource, providerimagepath=providerimagepath, package=package, providersource=providersource, environmentsource=environmentsource, overridevalue=overridevalue, environmentvalue=environmentvalue, providervalue=providervalue)
