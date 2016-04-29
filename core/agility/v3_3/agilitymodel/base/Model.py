from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ModelBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[], price=None, buildmodel=None, resources=[], cloud=None, modelid=None, architecture=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'price': {'native': True, 'name': 'price', 'minOccurs': '0', 'type': 'double'}, 'modelId': {'native': True, 'name': 'modelid', 'minOccurs': '0', 'type': 'string'}, 'buildModel': {'native': True, 'name': 'buildmodel', 'minOccurs': '0', 'type': 'boolean'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'Resource'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'architecture': {'native': False, 'name': 'architecture', 'minOccurs': '0', 'type': 'Architecture'}})
        self.properties = properties
        self.price = price
        self.buildmodel = buildmodel
        self.resources = resources
        self.cloud = cloud
        self.modelid = modelid
        self.architecture = architecture 
