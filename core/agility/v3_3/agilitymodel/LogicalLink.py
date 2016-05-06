from core.agility.v3_3.agilitymodel.base.LogicalLink import LogicalLinkBase
from core.agility.v3_3.agilitymodel.actions.LogicalLink import LogicalLinkActions

class LogicalLink(LogicalLinkBase, LogicalLinkActions):
    '''
    classdocs
    '''
    def __init__(self, logicalid=None):
        '''
        Constructor
        @param logicalid: logicalid minOccurs=0
        @type logicalid: string
        '''
        LogicalLinkBase.__init__(self, logicalid=logicalid)
