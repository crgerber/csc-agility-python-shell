from core.agility.v3_3.agilitymodel.base.ScriptUsage import ScriptUsageBase
from core.agility.v3_3.agilitymodel.actions.ScriptUsage import ScriptUsageActions

class ScriptUsage(ScriptUsageBase, ScriptUsageActions):
    '''
    classdocs
    '''
    def __init__(self, script=None, package=None, category=None):
        '''
        Constructor
        @param script: script minOccurs=0
        @type script: Script
        @param package: package minOccurs=0
        @type package: Package
        @param category: category minOccurs=0
        @type category: string
        '''
        ScriptUsageBase.__init__(self, script=script, package=package, category=category)
