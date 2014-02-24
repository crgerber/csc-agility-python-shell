from Item import ItemBase

class AccessUriBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, type=None, accessUri=None, accessUriExpanded=None, label=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'int', 'name': 'type', 'minOccurs': '0', 'native': True}, 'accessUri': {'type': 'string', 'name': 'accessUri', 'minOccurs': '0', 'native': True}, 'accessUriExpanded': {'type': 'string', 'name': 'accessUriExpanded', 'minOccurs': '0', 'native': True}, 'label': {'type': 'string', 'name': 'label', 'minOccurs': '0', 'native': True}})
        self.type = type
        self.accessUri = accessUri
        self.accessUriExpanded = accessUriExpanded
        self.label = label 
