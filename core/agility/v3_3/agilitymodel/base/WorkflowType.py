from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTypeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}})
        self.name = name
        self.description = description
        self.id = id 
