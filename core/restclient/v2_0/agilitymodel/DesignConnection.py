from core.restclient.v2_0.agilitymodel.base.DesignConnection import DesignConnectionBase
from core.restclient.v2_0.agilitymodel.actions.DesignConnection import DesignConnectionActions

class DesignConnection(DesignConnectionBase, DesignConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, srcLogicalId=None, destLogicalId=None, srcId=None, destId=None):
        '''
        Constructor
        @param srcLogicalId: srcLogicalId minOccurs=0
        @type srcLogicalId: string
        @param destLogicalId: destLogicalId minOccurs=0
        @type destLogicalId: string
        @param srcId: srcId minOccurs=0
        @type srcId: int
        @param destId: destId minOccurs=0
        @type destId: int
        '''
        DesignConnectionBase.__init__(self, srcLogicalId=srcLogicalId, destLogicalId=destLogicalId, srcId=srcId, destId=destId)
