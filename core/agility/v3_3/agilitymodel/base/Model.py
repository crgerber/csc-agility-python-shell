from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ModelBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, buildmodel=None, price=None, resources=[], architecture=None, properties=[], cloud=None, modelid=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'buildModel': {'type': 'boolean', 'name': 'buildmodel', 'minOccurs': '0', 'native': True}, 'price': {'type': 'double', 'name': 'price', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'modelId': {'type': 'string', 'name': 'modelid', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'architecture': {'type': 'Architecture', 'name': 'architecture', 'minOccurs': '0', 'native': False}})
        self.buildmodel = buildmodel
        self.price = price
        self.resources = resources
        self.architecture = architecture
        self.properties = properties
        self.cloud = cloud
        self.modelid = modelid 
