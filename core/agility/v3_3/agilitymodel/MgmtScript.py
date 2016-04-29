from core.agility.v3_3.agilitymodel.base.MgmtScript import MgmtScriptBase
from core.agility.v3_3.agilitymodel.actions.MgmtScript import MgmtScriptActions

class MgmtScript(MgmtScriptBase, MgmtScriptActions):
    '''
    classdocs
    '''
    def __init__(self, mgmtscripttype='', script=None, filesystem=None):
        '''
        Constructor
        @param mgmtscripttype: mgmtscripttype
        @type mgmtscripttype: string
        @param script: script
        @type script: Link
        @param filesystem: filesystem minOccurs=0
        @type filesystem: Link
        '''
        MgmtScriptBase.__init__(self, mgmtscripttype=mgmtscripttype, script=script, filesystem=filesystem)
