from core.agility.v2_0.agilitymodel.base.LogicalLink import LogicalLinkBase
from core.agility.v2_0.agilitymodel.actions.LogicalLink import LogicalLinkActions

class LogicalLink(LogicalLinkBase, LogicalLinkActions):
    '''
    classdocs
    '''
    def __init__(self, logicalId=None):
        '''
        Constructor
        @param logicalId: logicalId minOccurs=0
        @type logicalId: string
        '''
        LogicalLinkBase.__init__(self, logicalId=logicalId)
