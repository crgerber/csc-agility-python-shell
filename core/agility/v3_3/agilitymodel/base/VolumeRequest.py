from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class VolumeRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, storage=[], operation=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instance': {'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Instance'}, 'storage': {'maxOccurs': 'unbounded', 'native': False, 'name': 'storage', 'minOccurs': '0', 'type': 'Link'}, 'operation': {'native': False, 'name': 'operation', 'type': 'VolumeOperation'}})
        self.instance = instance
        self.storage = storage
        self.operation = operation 
