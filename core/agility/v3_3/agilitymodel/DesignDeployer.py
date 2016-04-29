from core.agility.v3_3.agilitymodel.base.DesignDeployer import DesignDeployerBase
from core.agility.v3_3.agilitymodel.actions.DesignDeployer import DesignDeployerActions

class DesignDeployer(DesignDeployerBase, DesignDeployerActions):
    '''
    classdocs
    '''
    def __init__(self, deployscript=None, stopscript=None, artifacttype=None, startscript=None, undeployscript=None, designcontainer=None, urlprefix=None, workloads=[]):
        '''
        Constructor
        @param deployscript: deployscript minOccurs=0
        @type deployscript: Link
        @param stopscript: stopscript minOccurs=0
        @type stopscript: Link
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param startscript: startscript minOccurs=0
        @type startscript: Link
        @param undeployscript: undeployscript minOccurs=0
        @type undeployscript: Link
        @param designcontainer: designcontainer minOccurs=0
        @type designcontainer: Link
        @param urlprefix: urlprefix minOccurs=0
        @type urlprefix: string
        @param workloads: workloads minOccurs=0 maxOccurs=unbounded
        @type workloads: LogicalLink
        '''
        DesignDeployerBase.__init__(self, deployscript=deployscript, stopscript=stopscript, artifacttype=artifacttype, startscript=startscript, undeployscript=undeployscript, designcontainer=designcontainer, urlprefix=urlprefix, workloads=workloads)
