from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ModelBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, properties=[], buildmodel=None, price=None, resources=[], modelid=None, architecture=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'buildModel': {'name': 'buildmodel', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'price': {'name': 'price', 'minOccurs': '0', 'native': True, 'type': 'double'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Resource'}, 'modelId': {'name': 'modelid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'architecture': {'name': 'architecture', 'minOccurs': '0', 'native': False, 'type': 'Architecture'}})
        self.cloud = cloud
        self.properties = properties
        self.buildmodel = buildmodel
        self.price = price
        self.resources = resources
        self.modelid = modelid
        self.architecture = architecture 
