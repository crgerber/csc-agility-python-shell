from core.agility.v3_3.agilitymodel.base.LaunchItem import LaunchItemBase

class LaunchItemDeploymentBase(LaunchItemBase):
    '''
    classdocs
    '''
    def __init__(self, launchitem=None, deployedon=None, variable=[], deployedby=None, deploymentplan=None):
        LaunchItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'launchItem': {'native': False, 'name': 'launchitem', 'minOccurs': '0', 'type': 'Link'}, 'deployedOn': {'native': True, 'name': 'deployedon', 'minOccurs': '0', 'type': 'date'}, 'deploymentPlan': {'native': True, 'name': 'deploymentplan', 'minOccurs': '0', 'type': 'string'}, 'variable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variable', 'minOccurs': '0', 'type': 'AssetProperty'}, 'deployedBy': {'native': False, 'name': 'deployedby', 'minOccurs': '0', 'type': 'Link'}})
        self.launchitem = launchitem
        self.deployedon = deployedon
        self.variable = variable
        self.deployedby = deployedby
        self.deploymentplan = deploymentplan 
