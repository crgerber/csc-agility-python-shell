from core.agility.common.AgilityModelBase import AgilityModelBase

class PageLayoutGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, gridclass='', description='', controls=[], showheader=False, name='', id=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'gridClass': {'native': True, 'name': 'gridclass', 'type': 'string'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'controls': {'maxOccurs': 'unbounded', 'native': False, 'name': 'controls', 'minOccurs': '0', 'type': 'Control'}, 'showHeader': {'native': True, 'name': 'showheader', 'type': 'boolean'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.gridclass = gridclass
        self.description = description
        self.controls = controls
        self.showheader = showheader
        self.name = name
        self.id = id
        self.type = type 
