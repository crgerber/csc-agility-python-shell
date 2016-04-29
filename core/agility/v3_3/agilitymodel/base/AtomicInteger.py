from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AtomicIntegerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, base=None, maxatomicvalue=None, uppercase=None, width=None, allowwrap=None, pkey=None, value=None, minatomicvalue=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'base': {'native': True, 'name': 'base', 'minOccurs': '0', 'type': 'byte'}, 'minAtomicValue': {'native': True, 'name': 'minatomicvalue', 'minOccurs': '0', 'type': 'long'}, 'maxAtomicValue': {'native': True, 'name': 'maxatomicvalue', 'minOccurs': '0', 'type': 'long'}, 'width': {'native': True, 'name': 'width', 'minOccurs': '0', 'type': 'byte'}, 'pkey': {'native': True, 'name': 'pkey', 'minOccurs': '0', 'type': 'string'}, 'allowWrap': {'native': True, 'name': 'allowwrap', 'minOccurs': '0', 'type': 'boolean'}, 'value': {'native': True, 'name': 'value', 'minOccurs': '0', 'type': 'string'}, 'upperCase': {'native': True, 'name': 'uppercase', 'minOccurs': '0', 'type': 'boolean'}})
        self.base = base
        self.maxatomicvalue = maxatomicvalue
        self.uppercase = uppercase
        self.width = width
        self.allowwrap = allowwrap
        self.pkey = pkey
        self.value = value
        self.minatomicvalue = minatomicvalue 
