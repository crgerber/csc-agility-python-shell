from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class LocationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, repositories=[], parentlocation=None, cloud=None, properties=[], sublocations=[], hosts=[], networks=[], storageroot=None, visible=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'repositories': {'name': 'repositories', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'parentLocation': {'name': 'parentlocation', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'visible': {'name': 'visible', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'sublocations': {'name': 'sublocations', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'hosts': {'name': 'hosts', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Host'}, 'storageRoot': {'name': 'storageroot', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'networks': {'name': 'networks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.repositories = repositories
        self.parentlocation = parentlocation
        self.cloud = cloud
        self.properties = properties
        self.sublocations = sublocations
        self.hosts = hosts
        self.networks = networks
        self.storageroot = storageroot
        self.visible = visible 
