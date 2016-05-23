from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTypeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', description=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}})
        self.id = id
        self.name = name
        self.description = description 
