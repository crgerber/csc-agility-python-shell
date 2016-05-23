from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class TargetCloudBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, models=[], template=None, stack=None, maxinstances=None, status=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'models': {'name': 'models', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'template': {'name': 'template', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'stack': {'name': 'stack', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'maxInstances': {'name': 'maxinstances', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.cloud = cloud
        self.models = models
        self.template = template
        self.stack = stack
        self.maxinstances = maxinstances
        self.status = status 
