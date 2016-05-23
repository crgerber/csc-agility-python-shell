from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, plan=None, variable=[], checkuse=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'plan': {'name': 'plan', 'native': False, 'type': 'DeploymentPlan'}, 'variable': {'name': 'variable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'checkUse': {'name': 'checkuse', 'native': True, 'type': 'boolean'}})
        self.plan = plan
        self.variable = variable
        self.checkuse = checkuse 
