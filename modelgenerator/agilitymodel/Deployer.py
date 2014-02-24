from base.Deployer import DeployerBase
from actions.Deployer import DeployerActions

class Deployer(DeployerBase, DeployerActions):
    '''
    classdocs
    '''
    def __init__(self, deployScript=None, templates=list(), startScript=None, urlPrefix=None, stopScript=None, undeployScript=None, artifactType=None):
        '''
        Constructor
        @param deployScript: deployScript minOccurs=0
        @type deployScript: Link
        @param templates: templates minOccurs=0 maxOccurs=unbounded
        @type templates: Link
        @param startScript: startScript minOccurs=0
        @type startScript: Link
        @param urlPrefix: urlPrefix minOccurs=0
        @type urlPrefix: string
        @param stopScript: stopScript minOccurs=0
        @type stopScript: Link
        @param undeployScript: undeployScript minOccurs=0
        @type undeployScript: Link
        @param artifactType: artifactType minOccurs=0
        @type artifactType: Link
        '''
        DeployerBase.__init__(self, deployScript=deployScript, templates=templates, startScript=startScript, urlPrefix=urlPrefix, stopScript=stopScript, undeployScript=undeployScript, artifactType=artifactType)
