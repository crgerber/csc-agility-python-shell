from core.agility.v3_3.agilitymodel.base.DesignAlias import DesignAliasBase
from core.agility.v3_3.agilitymodel.actions.DesignAlias import DesignAliasActions

class DesignAlias(DesignAliasBase, DesignAliasActions):
    '''
    classdocs
    '''
    def __init__(self, workloadlogicalid=None, workloadid=None):
        '''
        Constructor
        @param workloadlogicalid: workloadlogicalid minOccurs=0
        @type workloadlogicalid: string
        @param workloadid: workloadid minOccurs=0
        @type workloadid: int
        '''
        DesignAliasBase.__init__(self, workloadlogicalid=workloadlogicalid, workloadid=workloadid)
