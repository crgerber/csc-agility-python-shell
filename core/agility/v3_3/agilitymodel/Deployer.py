from core.agility.v3_3.agilitymodel.base.Deployer import DeployerBase
from core.agility.v3_3.agilitymodel.actions.Deployer import DeployerActions

class Deployer(DeployerBase, DeployerActions):
    '''
    classdocs
    '''
    def __init__(self, deployscript=None, templates=[], stopscript=None, artifacttype=None, startscript=None, undeployscript=None, urlprefix=None):
        '''
        Constructor
        @param deployscript: deployscript minOccurs=0
        @type deployscript: Link
        @param templates: templates minOccurs=0 maxOccurs=unbounded
        @type templates: Link
        @param stopscript: stopscript minOccurs=0
        @type stopscript: Link
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        @param startscript: startscript minOccurs=0
        @type startscript: Link
        @param undeployscript: undeployscript minOccurs=0
        @type undeployscript: Link
        @param urlprefix: urlprefix minOccurs=0
        @type urlprefix: string
        '''
        DeployerBase.__init__(self, deployscript=deployscript, templates=templates, stopscript=stopscript, artifacttype=artifacttype, startscript=startscript, undeployscript=undeployscript, urlprefix=urlprefix)
