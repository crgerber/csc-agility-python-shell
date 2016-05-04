from core.agility.common.AgilityModelBase import AgilityModelBase

class PageLayoutGroupBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, gridclass='', description='', showheader=False, controls=[], type='', id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'gridClass': {'type': 'string', 'name': 'gridclass', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'native': True}, 'controls': {'maxOccurs': 'unbounded', 'type': 'Control', 'name': 'controls', 'minOccurs': '0', 'native': False}, 'showHeader': {'type': 'boolean', 'name': 'showheader', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.gridclass = gridclass
        self.description = description
        self.showheader = showheader
        self.controls = controls
        self.type = type
        self.id = id
        self.name = name 
