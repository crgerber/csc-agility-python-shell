from core.agility.v3_3.agilitymodel.base.ScriptVariable import ScriptVariableBase
from core.agility.v3_3.agilitymodel.actions.ScriptVariable import ScriptVariableActions

class ScriptVariable(ScriptVariableBase, ScriptVariableActions):
    '''
    classdocs
    '''
    def __init__(self, overridevalue=None, providersource=None, projectsource=None, variablesource=None, projectvalue=None, environmentsource=None, providervalue=None, topologyvalue=None, package=[], environmentvalue=None, topologysource=None, script=[], providerimagepath=None):
        '''
        Constructor
        @param overridevalue: overridevalue minOccurs=0
        @type overridevalue: Variable
        @param providersource: providersource minOccurs=0
        @type providersource: string
        @param projectsource: projectsource minOccurs=0
        @type projectsource: string
        @param variablesource: variablesource minOccurs=0
        @type variablesource: string
        @param projectvalue: projectvalue minOccurs=0
        @type projectvalue: Variable
        @param environmentsource: environmentsource minOccurs=0
        @type environmentsource: string
        @param providervalue: providervalue minOccurs=0
        @type providervalue: Variable
        @param topologyvalue: topologyvalue minOccurs=0
        @type topologyvalue: Variable
        @param package: package minOccurs=0 maxOccurs=unbounded
        @type package: Link
        @param environmentvalue: environmentvalue minOccurs=0
        @type environmentvalue: Variable
        @param topologysource: topologysource minOccurs=0
        @type topologysource: string
        @param script: script minOccurs=0 maxOccurs=unbounded
        @type script: Link
        @param providerimagepath: providerimagepath minOccurs=0
        @type providerimagepath: string
        '''
        ScriptVariableBase.__init__(self, overridevalue=overridevalue, providersource=providersource, projectsource=projectsource, variablesource=variablesource, projectvalue=projectvalue, environmentsource=environmentsource, providervalue=providervalue, topologyvalue=topologyvalue, package=package, environmentvalue=environmentvalue, topologysource=topologysource, script=script, providerimagepath=providerimagepath)
