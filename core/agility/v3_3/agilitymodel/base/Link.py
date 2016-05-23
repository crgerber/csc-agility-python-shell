from core.agility.v3_3.agilitymodel.base.Baselink import BaselinkBase

class LinkBase(BaselinkBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, rel='', position=None, linkproperty=[], type=''):
        BaselinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'rel': {'name': 'rel', 'native': True, 'type': 'string'}, 'position': {'name': 'position', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}, 'linkProperty': {'name': 'linkproperty', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'NameValuePair'}})
        self.id = id
        self.rel = rel
        self.position = position
        self.linkproperty = linkproperty
        self.type = type 
