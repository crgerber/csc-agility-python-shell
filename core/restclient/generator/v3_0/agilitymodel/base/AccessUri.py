from .Item import ItemBase

class AccessUriBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, type=None, accessuri=None, accessuriexpanded=None, label=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'int', 'name': 'type', 'minOccurs': '0', 'native': True}, 'accessUri': {'type': 'string', 'name': 'accessuri', 'minOccurs': '0', 'native': True}, 'accessUriExpanded': {'type': 'string', 'name': 'accessuriexpanded', 'minOccurs': '0', 'native': True}, 'label': {'type': 'string', 'name': 'label', 'minOccurs': '0', 'native': True}})
        self.type = type
        self.accessuri = accessuri
        self.accessuriexpanded = accessuriexpanded
        self.label = label 
