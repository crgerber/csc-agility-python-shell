from core.agility.v3_3.agilitymodel.base.DesignAlias import DesignAliasBase
from core.agility.v3_3.agilitymodel.actions.DesignAlias import DesignAliasActions

class DesignAlias(DesignAliasBase, DesignAliasActions):
    '''
    classdocs
    '''
    def __init__(self, workloadid=None, workloadlogicalid=None):
        '''
        Constructor
        @param workloadid: workloadid minOccurs=0
        @type workloadid: int
        @param workloadlogicalid: workloadlogicalid minOccurs=0
        @type workloadlogicalid: string
        '''
        DesignAliasBase.__init__(self, workloadid=workloadid, workloadlogicalid=workloadlogicalid)
