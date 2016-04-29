from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, checkuse=False, plan=None, variable=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'checkUse': {'native': True, 'name': 'checkuse', 'type': 'boolean'}, 'plan': {'native': False, 'name': 'plan', 'type': 'DeploymentPlan'}, 'variable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variable', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.checkuse = checkuse
        self.plan = plan
        self.variable = variable 
