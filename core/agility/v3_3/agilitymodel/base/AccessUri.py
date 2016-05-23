from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AccessUriBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, accessuriexpanded=None, accessuri=None, label=None, type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'accessUriExpanded': {'name': 'accessuriexpanded', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'accessUri': {'name': 'accessuri', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'label': {'name': 'label', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.accessuriexpanded = accessuriexpanded
        self.accessuri = accessuri
        self.label = label
        self.type = type 
