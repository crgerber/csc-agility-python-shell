from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AccessUriBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, label=None, accessuriexpanded=None, accessuri=None, type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'label': {'native': True, 'name': 'label', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'int'}, 'accessUri': {'native': True, 'name': 'accessuri', 'minOccurs': '0', 'type': 'string'}, 'accessUriExpanded': {'native': True, 'name': 'accessuriexpanded', 'minOccurs': '0', 'type': 'string'}})
        self.label = label
        self.accessuriexpanded = accessuriexpanded
        self.accessuri = accessuri
        self.type = type 
