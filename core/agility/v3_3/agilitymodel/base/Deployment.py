from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DeploymentBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, readyforpromotion=None, environment=None, state=None, sourcedeployment=None, submitter=None, deploymentbindings=[], releaselabel=None, configuration=None, submitcomment=None, variables=[], releaseid=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'readyForPromotion': {'name': 'readyforpromotion', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'environment': {'name': 'environment', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'state': {'name': 'state', 'minOccurs': '0', 'native': False, 'type': 'DeploymentState'}, 'sourceDeployment': {'name': 'sourcedeployment', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'submitter': {'name': 'submitter', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'deploymentBindings': {'name': 'deploymentbindings', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DeploymentBinding'}, 'releaseLabel': {'name': 'releaselabel', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'configuration': {'name': 'configuration', 'minOccurs': '0', 'native': False, 'type': 'DeploymentConfiguration'}, 'submitComment': {'name': 'submitcomment', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'releaseId': {'name': 'releaseid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.readyforpromotion = readyforpromotion
        self.environment = environment
        self.state = state
        self.sourcedeployment = sourcedeployment
        self.submitter = submitter
        self.deploymentbindings = deploymentbindings
        self.releaselabel = releaselabel
        self.configuration = configuration
        self.submitcomment = submitcomment
        self.variables = variables
        self.releaseid = releaseid 
