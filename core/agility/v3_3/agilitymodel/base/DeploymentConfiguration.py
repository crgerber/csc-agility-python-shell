from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentConfigurationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}})
        self.id = id 
