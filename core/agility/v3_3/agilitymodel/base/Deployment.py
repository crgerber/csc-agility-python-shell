from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DeploymentBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, submitter=None, configuration=None, environment=None, deploymentbindings=[], releaseid=None, sourcedeployment=None, releaselabel=None, readyforpromotion=None, submitcomment=None, state=None, variables=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'submitter': {'native': False, 'name': 'submitter', 'minOccurs': '0', 'type': 'Link'}, 'configuration': {'native': False, 'name': 'configuration', 'minOccurs': '0', 'type': 'DeploymentConfiguration'}, 'environment': {'native': False, 'name': 'environment', 'minOccurs': '0', 'type': 'Link'}, 'deploymentBindings': {'maxOccurs': 'unbounded', 'native': False, 'name': 'deploymentbindings', 'minOccurs': '0', 'type': 'DeploymentBinding'}, 'releaseId': {'native': True, 'name': 'releaseid', 'minOccurs': '0', 'type': 'string'}, 'sourceDeployment': {'native': False, 'name': 'sourcedeployment', 'minOccurs': '0', 'type': 'Link'}, 'releaseLabel': {'native': True, 'name': 'releaselabel', 'minOccurs': '0', 'type': 'string'}, 'readyForPromotion': {'native': True, 'name': 'readyforpromotion', 'minOccurs': '0', 'type': 'boolean'}, 'submitComment': {'native': True, 'name': 'submitcomment', 'minOccurs': '0', 'type': 'string'}, 'state': {'native': False, 'name': 'state', 'minOccurs': '0', 'type': 'DeploymentState'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.submitter = submitter
        self.configuration = configuration
        self.environment = environment
        self.deploymentbindings = deploymentbindings
        self.releaseid = releaseid
        self.sourcedeployment = sourcedeployment
        self.releaselabel = releaselabel
        self.readyforpromotion = readyforpromotion
        self.submitcomment = submitcomment
        self.state = state
        self.variables = variables 
