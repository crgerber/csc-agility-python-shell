from core.agility.v3_3.agilitymodel.base.Deployer import DeployerBase
from core.agility.v3_3.agilitymodel.actions.Deployer import DeployerActions

class Deployer(DeployerBase, DeployerActions):
    '''
    classdocs
    '''
    def __init__(self, startscript=None, stopscript=None, undeployscript=None, templates=[], artifacttype=None, deployscript=None, urlprefix=None):
        '''
        Constructor
        @param startscript: startscript minOccurs=0
        @type startscript: Link
        @param stopscript: stopscript minOccurs=0
        @type stopscript: Link
        @param undeployscript: undeployscript minOccurs=0
        @type undeployscript: Link
        @param templates: templates minOccurs=0 maxOccurs=unbounded
        @type templates: Link
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param deployscript: deployscript minOccurs=0
        @type deployscript: Link
        @param urlprefix: urlprefix minOccurs=0
        @type urlprefix: string
        '''
        DeployerBase.__init__(self, startscript=startscript, stopscript=stopscript, undeployscript=undeployscript, templates=templates, artifacttype=artifacttype, deployscript=deployscript, urlprefix=urlprefix)
