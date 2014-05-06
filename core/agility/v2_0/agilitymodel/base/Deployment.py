from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class DeploymentBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, environment=None, deploymentBindings=list(), sourceDeployment=None, releaseLabel=None, submitComment=None, readyForPromotion=None, releaseId=None, state=None, submitter=None, configuration=None, variables=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'readyForPromotion': {'type': 'boolean', 'name': 'readyForPromotion', 'minOccurs': '0', 'native': True}, 'deploymentBindings': {'maxOccurs': 'unbounded', 'type': 'DeploymentBinding', 'name': 'deploymentBindings', 'minOccurs': '0', 'native': False}, 'sourceDeployment': {'type': 'Link', 'name': 'sourceDeployment', 'minOccurs': '0', 'native': False}, 'releaseLabel': {'type': 'string', 'name': 'releaseLabel', 'minOccurs': '0', 'native': True}, 'state': {'type': 'DeploymentState', 'name': 'state', 'minOccurs': '0', 'native': False}, 'environment': {'type': 'Link', 'name': 'environment', 'minOccurs': '0', 'native': False}, 'releaseId': {'type': 'string', 'name': 'releaseId', 'minOccurs': '0', 'native': True}, 'submitComment': {'type': 'string', 'name': 'submitComment', 'minOccurs': '0', 'native': True}, 'submitter': {'type': 'Link', 'name': 'submitter', 'minOccurs': '0', 'native': False}, 'configuration': {'type': 'DeploymentConfiguration', 'name': 'configuration', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}})
        self.environment = environment
        self.deploymentBindings = deploymentBindings
        self.sourceDeployment = sourceDeployment
        self.releaseLabel = releaseLabel
        self.submitComment = submitComment
        self.readyForPromotion = readyForPromotion
        self.releaseId = releaseId
        self.state = state
        self.submitter = submitter
        self.configuration = configuration
        self.variables = variables 
