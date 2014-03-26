from core.agility.common.AgilityModelBase import AgilityModelBase


class WorkflowTaskMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, pathicon='', icon='', transitions=[], name='', description=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'type': 'string', 'name': 'description', 'native': True}, 'pathIcon': {'type': 'string', 'name': 'pathicon', 'native': True}, 'transitions': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'transitions', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'icon': {'type': 'string', 'name': 'icon', 'native': True}})
        self.pathicon = pathicon
        self.icon = icon
        self.transitions = transitions
        self.name = name
        self.description = description 
