from core.agility.v3_3.agilitymodel.base.DesignDeployer import DesignDeployerBase
from core.agility.v3_3.agilitymodel.actions.DesignDeployer import DesignDeployerActions

class DesignDeployer(DesignDeployerBase, DesignDeployerActions):
    '''
    classdocs
    '''
    def __init__(self, startscript=None, stopscript=None, undeployscript=None, workloads=[], artifacttype=None, deployscript=None, designcontainer=None, urlprefix=None):
        '''
        Constructor
        @param startscript: startscript minOccurs=0
        @type startscript: Link
        @param stopscript: stopscript minOccurs=0
        @type stopscript: Link
        @param undeployscript: undeployscript minOccurs=0
        @type undeployscript: Link
        @param workloads: workloads minOccurs=0 maxOccurs=unbounded
        @type workloads: LogicalLink
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param deployscript: deployscript minOccurs=0
        @type deployscript: Link
        @param designcontainer: designcontainer minOccurs=0
        @type designcontainer: Link
        @param urlprefix: urlprefix minOccurs=0
        @type urlprefix: string
        '''
        DesignDeployerBase.__init__(self, startscript=startscript, stopscript=stopscript, undeployscript=undeployscript, workloads=workloads, artifacttype=artifacttype, deployscript=deployscript, designcontainer=designcontainer, urlprefix=urlprefix)
