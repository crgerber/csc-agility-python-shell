from core.agility.common.AgilityModelBase import AgilityModelBase


class LinkBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', linkproperty=[], href='', rel='', position=None, type='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'type': 'string', 'name': 'name', 'native': True}, 'linkProperty': {'maxOccurs': 'unbounded', 'type': 'NameValuePair', 'name': 'linkproperty', 'minOccurs': '0', 'native': False}, 'href': {'type': 'string', 'name': 'href', 'native': True}, 'rel': {'type': 'string', 'name': 'rel', 'native': True}, 'position': {'type': 'int', 'name': 'position', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.name = name
        self.linkproperty = linkproperty
        self.href = href
        self.rel = rel
        self.position = position
        self.type = type
        self.id = id 
