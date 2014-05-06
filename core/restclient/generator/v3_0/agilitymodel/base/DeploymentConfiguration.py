from AgilityModelBase import AgilityModelBase

class DeploymentConfigurationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.id = id 
