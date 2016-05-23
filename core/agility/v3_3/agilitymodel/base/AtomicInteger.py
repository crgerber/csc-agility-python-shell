from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AtomicIntegerBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, width=None, value=None, maxatomicvalue=None, pkey=None, minatomicvalue=None, uppercase=None, allowwrap=None, base=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'width': {'name': 'width', 'minOccurs': '0', 'native': True, 'type': 'byte'}, 'value': {'name': 'value', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'maxAtomicValue': {'name': 'maxatomicvalue', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'upperCase': {'name': 'uppercase', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'minAtomicValue': {'name': 'minatomicvalue', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'pkey': {'name': 'pkey', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'allowWrap': {'name': 'allowwrap', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'base': {'name': 'base', 'minOccurs': '0', 'native': True, 'type': 'byte'}})
        self.width = width
        self.value = value
        self.maxatomicvalue = maxatomicvalue
        self.pkey = pkey
        self.minatomicvalue = minatomicvalue
        self.uppercase = uppercase
        self.allowwrap = allowwrap
        self.base = base 
