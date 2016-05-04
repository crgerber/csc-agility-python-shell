from LaunchItem import LaunchItemBase

class LaunchItemDeploymentBase(LaunchItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployedon=None, variable=[], deployedby=None, launchitem=None, deploymentplan=None):
        LaunchItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'deployedBy': {'type': 'Link', 'name': 'deployedby', 'minOccurs': '0', 'native': False}, 'deployedOn': {'type': 'date', 'name': 'deployedon', 'minOccurs': '0', 'native': True}, 'deploymentPlan': {'type': 'string', 'name': 'deploymentplan', 'minOccurs': '0', 'native': True}, 'launchItem': {'type': 'Link', 'name': 'launchitem', 'minOccurs': '0', 'native': False}})
        self.deployedon = deployedon
        self.variable = variable
        self.deployedby = deployedby
        self.launchitem = launchitem
        self.deploymentplan = deploymentplan 
