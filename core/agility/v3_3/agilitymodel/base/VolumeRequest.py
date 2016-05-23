from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class VolumeRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, operation=None, storage=[]):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instance': {'name': 'instance', 'minOccurs': '0', 'native': False, 'type': 'Instance'}, 'operation': {'name': 'operation', 'native': False, 'type': 'VolumeOperation'}, 'storage': {'name': 'storage', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.instance = instance
        self.operation = operation
        self.storage = storage 
