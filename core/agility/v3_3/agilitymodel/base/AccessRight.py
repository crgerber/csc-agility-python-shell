from core.agility.common.AgilityModelBase import AgilityModelBase

class AccessRightBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name=None, granted=None, defaultgranted=None, source=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'granted': {'name': 'granted', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'defaultGranted': {'name': 'defaultgranted', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'source': {'name': 'source', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.id = id
        self.name = name
        self.granted = granted
        self.defaultgranted = defaultgranted
        self.source = source 
