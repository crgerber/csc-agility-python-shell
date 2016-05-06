from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AtomicIntegerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, pkey=None, allowwrap=None, minatomicvalue=None, uppercase=None, value=None, width=None, base=None, maxatomicvalue=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'pkey': {'type': 'string', 'name': 'pkey', 'minOccurs': '0', 'native': True}, 'allowWrap': {'type': 'boolean', 'name': 'allowwrap', 'minOccurs': '0', 'native': True}, 'minAtomicValue': {'type': 'long', 'name': 'minatomicvalue', 'minOccurs': '0', 'native': True}, 'upperCase': {'type': 'boolean', 'name': 'uppercase', 'minOccurs': '0', 'native': True}, 'value': {'type': 'string', 'name': 'value', 'minOccurs': '0', 'native': True}, 'width': {'type': 'byte', 'name': 'width', 'minOccurs': '0', 'native': True}, 'base': {'type': 'byte', 'name': 'base', 'minOccurs': '0', 'native': True}, 'maxAtomicValue': {'type': 'long', 'name': 'maxatomicvalue', 'minOccurs': '0', 'native': True}})
        self.pkey = pkey
        self.allowwrap = allowwrap
        self.minatomicvalue = minatomicvalue
        self.uppercase = uppercase
        self.value = value
        self.width = width
        self.base = base
        self.maxatomicvalue = maxatomicvalue 
