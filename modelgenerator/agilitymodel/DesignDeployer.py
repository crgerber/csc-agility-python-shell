from base.DesignDeployer import DesignDeployerBase
from actions.DesignDeployer import DesignDeployerActions

class DesignDeployer(DesignDeployerBase, DesignDeployerActions):
    '''
    classdocs
    '''
    def __init__(self, deployScript=None, startScript=None, designContainer=None, urlPrefix=None, stopScript=None, undeployScript=None, artifactType=None, workloads=list()):
        '''
        Constructor
        @param deployScript: deployScript minOccurs=0
        @type deployScript: Link
        @param startScript: startScript minOccurs=0
        @type startScript: Link
        @param designContainer: designContainer minOccurs=0
        @type designContainer: Link
        @param urlPrefix: urlPrefix minOccurs=0
        @type urlPrefix: string
        @param stopScript: stopScript minOccurs=0
        @type stopScript: Link
        @param undeployScript: undeployScript minOccurs=0
        @type undeployScript: Link
        @param artifactType: artifactType minOccurs=0
        @type artifactType: Link
        @param workloads: workloads minOccurs=0 maxOccurs=unbounded
        @type workloads: LogicalLink
        '''
        DesignDeployerBase.__init__(self, deployScript=deployScript, startScript=startScript, designContainer=designContainer, urlPrefix=urlPrefix, stopScript=stopScript, undeployScript=undeployScript, artifactType=artifactType, workloads=workloads)
