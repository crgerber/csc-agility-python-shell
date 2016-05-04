from ApiRequest import ApiRequestBase

class VolumeRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, operation=None, storage=[]):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instance': {'type': 'Instance', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'operation': {'type': 'VolumeOperation', 'name': 'operation', 'native': False}, 'storage': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'storage', 'minOccurs': '0', 'native': False}})
        self.instance = instance
        self.operation = operation
        self.storage = storage 
