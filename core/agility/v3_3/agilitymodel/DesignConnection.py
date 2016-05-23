from core.agility.v3_3.agilitymodel.base.DesignConnection import DesignConnectionBase
from core.agility.v3_3.agilitymodel.actions.DesignConnection import DesignConnectionActions

class DesignConnection(DesignConnectionBase, DesignConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, srcid=None, destid=None, srclogicalid=None, destlogicalid=None):
        '''
        Constructor
        @param srcid: srcid minOccurs=0
        @type srcid: int
        @param destid: destid minOccurs=0
        @type destid: int
        @param srclogicalid: srclogicalid minOccurs=0
        @type srclogicalid: string
        @param destlogicalid: destlogicalid minOccurs=0
        @type destlogicalid: string
        '''
        DesignConnectionBase.__init__(self, srcid=srcid, destid=destid, srclogicalid=srclogicalid, destlogicalid=destlogicalid)
