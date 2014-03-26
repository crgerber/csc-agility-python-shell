from base.DesignConnection import DesignConnectionBase
from actions.DesignConnection import DesignConnectionActions

class DesignConnection(DesignConnectionBase, DesignConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, srclogicalid=None, destlogicalid=None, srcid=None, destid=None):
        '''
        Constructor
        @param srclogicalid: srclogicalid minOccurs=0
        @type srclogicalid: string
        @param destlogicalid: destlogicalid minOccurs=0
        @type destlogicalid: string
        @param srcid: srcid minOccurs=0
        @type srcid: int
        @param destid: destid minOccurs=0
        @type destid: int
        '''
        DesignConnectionBase.__init__(self, srclogicalid=srclogicalid, destlogicalid=destlogicalid, srcid=srcid, destid=destid)
