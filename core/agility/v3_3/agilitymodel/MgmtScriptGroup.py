from core.agility.v3_3.agilitymodel.base.MgmtScriptGroup import MgmtScriptGroupBase
from core.agility.v3_3.agilitymodel.actions.MgmtScriptGroup import MgmtScriptGroupActions

class MgmtScriptGroup(MgmtScriptGroupBase, MgmtScriptGroupActions):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=None, mgmtscripts=[]):
        '''
        Constructor
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param mgmtscripts: mgmtscripts minOccurs=0 maxOccurs=unbounded
        @type mgmtscripts: MgmtScript
        '''
        MgmtScriptGroupBase.__init__(self, operatingsystem=operatingsystem, mgmtscripts=mgmtscripts)
