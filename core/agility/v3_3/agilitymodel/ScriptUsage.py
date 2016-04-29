from core.agility.v3_3.agilitymodel.base.ScriptUsage import ScriptUsageBase
from core.agility.v3_3.agilitymodel.actions.ScriptUsage import ScriptUsageActions

class ScriptUsage(ScriptUsageBase, ScriptUsageActions):
    '''
    classdocs
    '''
    def __init__(self, category=None, script=None, package=None):
        '''
        Constructor
        @param category: category minOccurs=0
        @type category: string
        @param script: script minOccurs=0
        @type script: Script
        @param package: package minOccurs=0
        @type package: Package
        '''
        ScriptUsageBase.__init__(self, category=category, script=script, package=package)
