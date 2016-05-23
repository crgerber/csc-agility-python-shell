from core.agility.v3_3.agilitymodel.base.LaunchItem import LaunchItemBase

class LaunchItemDeploymentBase(LaunchItemBase):
    '''
    classdocs
    '''
    def __init__(self, launchitem=None, variable=[], deployedby=None, deploymentplan=None, deployedon=None):
        LaunchItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'launchItem': {'name': 'launchitem', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'variable': {'name': 'variable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'deployedBy': {'name': 'deployedby', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'deploymentPlan': {'name': 'deploymentplan', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'deployedOn': {'name': 'deployedon', 'minOccurs': '0', 'native': True, 'type': 'date'}})
        self.launchitem = launchitem
        self.variable = variable
        self.deployedby = deployedby
        self.deploymentplan = deploymentplan
        self.deployedon = deployedon 
