from core.agility.v3_3.agilitymodel.base.ScriptVariable import ScriptVariableBase
from core.agility.v3_3.agilitymodel.actions.ScriptVariable import ScriptVariableActions

class ScriptVariable(ScriptVariableBase, ScriptVariableActions):
    '''
    classdocs
    '''
    def __init__(self, topologysource=None, projectsource=None, package=[], projectvalue=None, script=[], providervalue=None, providersource=None, overridevalue=None, providerimagepath=None, variablesource=None, environmentvalue=None, environmentsource=None, topologyvalue=None):
        '''
        Constructor
        @param topologysource: topologysource minOccurs=0
        @type topologysource: string
        @param projectsource: projectsource minOccurs=0
        @type projectsource: string
        @param package: package minOccurs=0 maxOccurs=unbounded
        @type package: Link
        @param projectvalue: projectvalue minOccurs=0
        @type projectvalue: Variable
        @param script: script minOccurs=0 maxOccurs=unbounded
        @type script: Link
        @param providervalue: providervalue minOccurs=0
        @type providervalue: Variable
        @param providersource: providersource minOccurs=0
        @type providersource: string
        @param overridevalue: overridevalue minOccurs=0
        @type overridevalue: Variable
        @param providerimagepath: providerimagepath minOccurs=0
        @type providerimagepath: string
        @param variablesource: variablesource minOccurs=0
        @type variablesource: string
        @param environmentvalue: environmentvalue minOccurs=0
        @type environmentvalue: Variable
        @param environmentsource: environmentsource minOccurs=0
        @type environmentsource: string
        @param topologyvalue: topologyvalue minOccurs=0
        @type topologyvalue: Variable
        '''
        ScriptVariableBase.__init__(self, topologysource=topologysource, projectsource=projectsource, package=package, projectvalue=projectvalue, script=script, providervalue=providervalue, providersource=providersource, overridevalue=overridevalue, providerimagepath=providerimagepath, variablesource=variablesource, environmentvalue=environmentvalue, environmentsource=environmentsource, topologyvalue=topologyvalue)
