from core.agility.v3_3.agilitymodel.base.Baselink import BaselinkBase

class LinkBase(BaselinkBase):
    '''
    classdocs
    '''
    def __init__(self, linkproperty=[], position=None, rel='', id=None, type=''):
        BaselinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'native': True, 'name': 'type', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'position': {'native': True, 'name': 'position', 'minOccurs': '0', 'type': 'int'}, 'linkProperty': {'maxOccurs': 'unbounded', 'native': False, 'name': 'linkproperty', 'minOccurs': '0', 'type': 'NameValuePair'}, 'rel': {'native': True, 'name': 'rel', 'type': 'string'}})
        self.linkproperty = linkproperty
        self.position = position
        self.rel = rel
        self.id = id
        self.type = type 
