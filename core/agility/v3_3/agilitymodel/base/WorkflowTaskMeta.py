from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTaskMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, pathicon='', name='', icon='', description='', transitions=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'pathIcon': {'native': True, 'name': 'pathicon', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'icon': {'native': True, 'name': 'icon', 'type': 'string'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'transitions': {'maxOccurs': 'unbounded', 'native': False, 'name': 'transitions', 'minOccurs': '0', 'type': 'Link'}})
        self.pathicon = pathicon
        self.name = name
        self.icon = icon
        self.description = description
        self.transitions = transitions 
