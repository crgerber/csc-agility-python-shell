from base.DesignAlias import DesignAliasBase
from actions.DesignAlias import DesignAliasActions

class DesignAlias(DesignAliasBase, DesignAliasActions):
    '''
    classdocs
    '''
    def __init__(self, workloadLogicalId=None, workloadId=None):
        '''
        Constructor
        @param workloadLogicalId: workloadLogicalId minOccurs=0
        @type workloadLogicalId: string
        @param workloadId: workloadId minOccurs=0
        @type workloadId: int
        '''
        DesignAliasBase.__init__(self, workloadLogicalId=workloadLogicalId, workloadId=workloadId)
