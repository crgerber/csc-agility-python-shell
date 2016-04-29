from core.agility.common.AgilityModelBase import AgilityModelBase

class DistNodePackageBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, version=None, name=None, status=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}})
        self.version = version
        self.name = name
        self.status = status
        self.id = id 
