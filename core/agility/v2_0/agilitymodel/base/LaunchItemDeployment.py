from core.agility.v2_0.agilitymodel.base.LaunchItem import LaunchItemBase

class LaunchItemDeploymentBase(LaunchItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployedOn=None, variable=list(), deployedBy=None, launchItem=None, deploymentPlan=None):
        LaunchItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'deployedBy': {'type': 'Link', 'name': 'deployedBy', 'minOccurs': '0', 'native': False}, 'deployedOn': {'type': 'date', 'name': 'deployedOn', 'minOccurs': '0', 'native': True}, 'deploymentPlan': {'type': 'string', 'name': 'deploymentPlan', 'minOccurs': '0', 'native': True}, 'launchItem': {'type': 'Link', 'name': 'launchItem', 'minOccurs': '0', 'native': False}})
        self.deployedOn = deployedOn
        self.variable = variable
        self.deployedBy = deployedBy
        self.launchItem = launchItem
        self.deploymentPlan = deploymentPlan 
