from base.LogicalLink import LogicalLinkBase
from actions.LogicalLink import LogicalLinkActions

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
