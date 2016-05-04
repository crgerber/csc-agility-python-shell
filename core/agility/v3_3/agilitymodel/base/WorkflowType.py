from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTypeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, description='', id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'type': 'string', 'name': 'description', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.description = description
        self.id = id
        self.name = name 
