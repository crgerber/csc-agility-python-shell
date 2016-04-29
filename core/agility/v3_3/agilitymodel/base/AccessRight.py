from core.agility.common.AgilityModelBase import AgilityModelBase

class AccessRightBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, granted=None, name=None, defaultgranted=None, source=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'granted': {'native': True, 'name': 'granted', 'minOccurs': '0', 'type': 'boolean'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'source': {'native': True, 'name': 'source', 'minOccurs': '0', 'type': 'string'}, 'defaultGranted': {'native': True, 'name': 'defaultgranted', 'minOccurs': '0', 'type': 'boolean'}})
        self.granted = granted
        self.name = name
        self.defaultgranted = defaultgranted
        self.source = source
        self.id = id 
