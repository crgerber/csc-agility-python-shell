from core.agility.common.AgilityModelBase import AgilityModelBase

class DistNodePackageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, version=None, id=None, name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.version = version
        self.id = id
        self.name = name 
