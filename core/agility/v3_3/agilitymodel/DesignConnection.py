from core.agility.v3_3.agilitymodel.base.DesignConnection import DesignConnectionBase
from core.agility.v3_3.agilitymodel.actions.DesignConnection import DesignConnectionActions

class DesignConnection(DesignConnectionBase, DesignConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, destlogicalid=None, destid=None, srclogicalid=None, srcid=None):
        '''
        Constructor
        @param destlogicalid: destlogicalid minOccurs=0
        @type destlogicalid: string
        @param destid: destid minOccurs=0
        @type destid: int
        @param srclogicalid: srclogicalid minOccurs=0
        @type srclogicalid: string
        @param srcid: srcid minOccurs=0
        @type srcid: int
        '''
        DesignConnectionBase.__init__(self, destlogicalid=destlogicalid, destid=destid, srclogicalid=srclogicalid, srcid=srcid)
