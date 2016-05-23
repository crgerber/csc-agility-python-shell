from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTaskMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', transitions=[], pathicon='', icon=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}, 'icon': {'name': 'icon', 'native': True, 'type': 'string'}, 'pathIcon': {'name': 'pathicon', 'native': True, 'type': 'string'}, 'transitions': {'name': 'transitions', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.name = name
        self.description = description
        self.transitions = transitions
        self.pathicon = pathicon
        self.icon = icon 
