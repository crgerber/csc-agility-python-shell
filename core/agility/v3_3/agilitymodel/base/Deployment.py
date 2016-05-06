from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DeploymentBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, environment=None, deploymentbindings=[], sourcedeployment=None, releaselabel=None, submitcomment=None, readyforpromotion=None, releaseid=None, state=None, submitter=None, configuration=None, variables=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'readyForPromotion': {'type': 'boolean', 'name': 'readyforpromotion', 'minOccurs': '0', 'native': True}, 'deploymentBindings': {'maxOccurs': 'unbounded', 'type': 'DeploymentBinding', 'name': 'deploymentbindings', 'minOccurs': '0', 'native': False}, 'sourceDeployment': {'type': 'Link', 'name': 'sourcedeployment', 'minOccurs': '0', 'native': False}, 'releaseLabel': {'type': 'string', 'name': 'releaselabel', 'minOccurs': '0', 'native': True}, 'state': {'type': 'DeploymentState', 'name': 'state', 'minOccurs': '0', 'native': False}, 'environment': {'type': 'Link', 'name': 'environment', 'minOccurs': '0', 'native': False}, 'releaseId': {'type': 'string', 'name': 'releaseid', 'minOccurs': '0', 'native': True}, 'submitComment': {'type': 'string', 'name': 'submitcomment', 'minOccurs': '0', 'native': True}, 'submitter': {'type': 'Link', 'name': 'submitter', 'minOccurs': '0', 'native': False}, 'configuration': {'type': 'DeploymentConfiguration', 'name': 'configuration', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}})
        self.environment = environment
        self.deploymentbindings = deploymentbindings
        self.sourcedeployment = sourcedeployment
        self.releaselabel = releaselabel
        self.submitcomment = submitcomment
        self.readyforpromotion = readyforpromotion
        self.releaseid = releaseid
        self.state = state
        self.submitter = submitter
        self.configuration = configuration
        self.variables = variables 
