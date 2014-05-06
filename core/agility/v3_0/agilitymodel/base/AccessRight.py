from core.agility.common.AgilityModelBase import AgilityModelBase


class AccessRightBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, source=None, defaultgranted=None, granted=None, id=None, name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'source': {'type': 'string', 'name': 'source', 'minOccurs': '0', 'native': True}, 'defaultGranted': {'type': 'boolean', 'name': 'defaultgranted', 'minOccurs': '0', 'native': True}, 'granted': {'type': 'boolean', 'name': 'granted', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}})
        self.source = source
        self.defaultgranted = defaultgranted
        self.granted = granted
        self.id = id
        self.name = name 
