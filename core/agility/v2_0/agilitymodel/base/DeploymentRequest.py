from core.agility.common.AgilityModelBase import AgilityModelBase


class DeploymentRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variable=list(), checkUse=False, plan=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'checkUse': {'type': 'boolean', 'name': 'checkUse', 'native': True}, 'plan': {'type': 'DeploymentPlan', 'name': 'plan', 'native': False}})
        self.variable = variable
        self.checkUse = checkUse
        self.plan = plan 
