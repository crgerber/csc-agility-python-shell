from core.agility.v3_3.agilitymodel.base.MgmtScript import MgmtScriptBase
from core.agility.v3_3.agilitymodel.actions.MgmtScript import MgmtScriptActions

class MgmtScript(MgmtScriptBase, MgmtScriptActions):
    '''
    classdocs
    '''
    def __init__(self, script=None, mgmtscripttype='', filesystem=None):
        '''
        Constructor
        @param script: script
        @type script: Link
        @param mgmtscripttype: mgmtscripttype
        @type mgmtscripttype: string
        @param filesystem: filesystem minOccurs=0
        @type filesystem: Link
        '''
        MgmtScriptBase.__init__(self, script=script, mgmtscripttype=mgmtscripttype, filesystem=filesystem)
