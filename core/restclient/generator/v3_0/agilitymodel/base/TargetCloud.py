from .Asset import AssetBase

class TargetCloudBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, maxinstances=None, models=[], template=None, stack=None, cloud=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'maxInstances': {'type': 'int', 'name': 'maxinstances', 'minOccurs': '0', 'native': True}, 'models': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'models', 'minOccurs': '0', 'native': False}, 'template': {'type': 'Link', 'name': 'template', 'minOccurs': '0', 'native': False}, 'stack': {'type': 'Link', 'name': 'stack', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.maxinstances = maxinstances
        self.models = models
        self.template = template
        self.stack = stack
        self.cloud = cloud 
