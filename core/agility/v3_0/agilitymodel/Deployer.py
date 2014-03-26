from core.agility.v3_0.agilitymodel.base.Deployer import DeployerBase
from core.agility.v3_0.agilitymodel.actions.Deployer import DeployerActions

class Deployer(DeployerBase, DeployerActions):
    '''
    classdocs
    '''
    def __init__(self, deployscript=None, templates=[], startscript=None, urlprefix=None, stopscript=None, undeployscript=None, artifacttype=None):
        '''
        Constructor
        @param deployscript: deployscript minOccurs=0
        @type deployscript: Link
        @param templates: templates minOccurs=0 maxOccurs=unbounded
        @type templates: Link
        @param startscript: startscript minOccurs=0
        @type startscript: Link
        @param urlprefix: urlprefix minOccurs=0
        @type urlprefix: string
        @param stopscript: stopscript minOccurs=0
        @type stopscript: Link
        @param undeployscript: undeployscript minOccurs=0
        @type undeployscript: Link
        @param artifacttype: artifacttype minOccurs=0
        @type artifacttype: Link
        '''
        DeployerBase.__init__(self, deployscript=deployscript, templates=templates, startscript=startscript, urlprefix=urlprefix, stopscript=stopscript, undeployscript=undeployscript, artifacttype=artifacttype)
