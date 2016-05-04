from base.ScriptUsage import ScriptUsageBase
from actions.ScriptUsage import ScriptUsageActions

class ScriptUsage(ScriptUsageBase, ScriptUsageActions):
    '''
    classdocs
    '''
    def __init__(self, category=None, package=None, script=None):
        '''
        Constructor
        @param category: category minOccurs=0
        @type category: string
        @param package: package minOccurs=0
        @type package: Package
        @param script: script minOccurs=0
        @type script: Script
        '''
        ScriptUsageBase.__init__(self, category=category, package=package, script=script)
