from core.agility.v3_3.agilitymodel.base.DesignDeployer import DesignDeployerBase
from core.agility.v3_3.agilitymodel.actions.DesignDeployer import DesignDeployerActions

class DesignDeployer(DesignDeployerBase, DesignDeployerActions):
    '''
    classdocs
    '''
    def __init__(self, deployscript=None, startscript=None, designcontainer=None, urlprefix=None, stopscript=None, undeployscript=None, artifacttype=None, workloads=[]):
        '''
        Constructor
        @param deployscript: deployscript minOccurs=0
        @type deployscript: Link
        @param startscript: startscript minOccurs=0
        @type startscript: Link
        @param designcontainer: designcontainer minOccurs=0
        @type designcontainer: Link
        @param urlprefix: urlprefix minOccurs=0
        @type urlprefix: string
        @param stopscript: stopscript minOccurs=0
        @type stopscript: Link
        @param undeployscript: undeployscript minOccurs=0
        @type undeployscript: Link
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param workloads: workloads minOccurs=0 maxOccurs=unbounded
        @type workloads: LogicalLink
        '''
        DesignDeployerBase.__init__(self, deployscript=deployscript, startscript=startscript, designcontainer=designcontainer, urlprefix=urlprefix, stopscript=stopscript, undeployscript=undeployscript, artifacttype=artifacttype, workloads=workloads)
