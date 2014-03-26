from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class ModelBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, price=None, architecture=None, resources=list(), buildModel=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'price': {'type': 'double', 'name': 'price', 'minOccurs': '0', 'native': True}, 'architecture': {'type': 'Architecture', 'name': 'architecture', 'minOccurs': '0', 'native': False}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'buildModel': {'type': 'boolean', 'name': 'buildModel', 'minOccurs': '0', 'native': True}, 'properties': {'type': 'Property', 'name': 'properties','maxOccurs': 'unbounded', 'minOccurs': '0', 'native': False}})
        self.price = price
        self.architecture = architecture
        self.resources = resources
        self.buildModel = buildModel 
