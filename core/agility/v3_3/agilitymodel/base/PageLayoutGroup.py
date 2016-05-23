from core.agility.common.AgilityModelBase import AgilityModelBase

class PageLayoutGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', gridclass='', controls=[], description='', id=None, showheader=False, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'name': 'type', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}, 'gridClass': {'name': 'gridclass', 'native': True, 'type': 'string'}, 'controls': {'name': 'controls', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Control'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'showHeader': {'name': 'showheader', 'native': True, 'type': 'boolean'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}})
        self.name = name
        self.gridclass = gridclass
        self.controls = controls
        self.description = description
        self.id = id
        self.showheader = showheader
        self.type = type 
