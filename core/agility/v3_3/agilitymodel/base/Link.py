from core.agility.v3_3.agilitymodel.base.Baselink import BaselinkBase

class LinkBase(BaselinkBase):
    '''
    classdocs
    '''
    def __init__(self, position=None, type='', id=None, rel='', linkproperty=[]):
        BaselinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'position': {'type': 'int', 'name': 'position', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'rel': {'type': 'string', 'name': 'rel', 'native': True}, 'linkProperty': {'maxOccurs': 'unbounded', 'type': 'NameValuePair', 'name': 'linkproperty', 'minOccurs': '0', 'native': False}})
        self.position = position
        self.type = type
        self.id = id
        self.rel = rel
        self.linkproperty = linkproperty 
