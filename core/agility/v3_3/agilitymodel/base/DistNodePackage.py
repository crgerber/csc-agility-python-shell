from core.agility.common.AgilityModelBase import AgilityModelBase

class DistNodePackageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name=None, status=None, version=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.id = id
        self.name = name
        self.status = status
        self.version = version 
