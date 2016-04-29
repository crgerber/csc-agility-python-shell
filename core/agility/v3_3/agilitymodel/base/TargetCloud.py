from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class TargetCloudBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, template=None, cloud=None, stack=None, maxinstances=None, models=[], status=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'template': {'native': False, 'name': 'template', 'minOccurs': '0', 'type': 'Link'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'stack': {'native': False, 'name': 'stack', 'minOccurs': '0', 'type': 'Link'}, 'maxInstances': {'native': True, 'name': 'maxinstances', 'minOccurs': '0', 'type': 'int'}, 'models': {'maxOccurs': 'unbounded', 'native': False, 'name': 'models', 'minOccurs': '0', 'type': 'Link'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}})
        self.template = template
        self.cloud = cloud
        self.stack = stack
        self.maxinstances = maxinstances
        self.models = models
        self.status = status 
