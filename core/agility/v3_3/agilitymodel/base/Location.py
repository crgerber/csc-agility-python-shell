from Item import ItemBase

class LocationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, repositories=[], properties=[], visible=None, parentlocation=None, hosts=[], cloud=None, storageroot=None, networks=[], sublocations=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'repositories': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'repositories', 'minOccurs': '0', 'native': False}, 'networks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networks', 'minOccurs': '0', 'native': False}, 'visible': {'type': 'boolean', 'name': 'visible', 'minOccurs': '0', 'native': True}, 'parentLocation': {'type': 'Link', 'name': 'parentlocation', 'minOccurs': '0', 'native': False}, 'hosts': {'maxOccurs': 'unbounded', 'type': 'Host', 'name': 'hosts', 'minOccurs': '0', 'native': False}, 'sublocations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'sublocations', 'minOccurs': '0', 'native': False}, 'storageRoot': {'type': 'boolean', 'name': 'storageroot', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.repositories = repositories
        self.properties = properties
        self.visible = visible
        self.parentlocation = parentlocation
        self.hosts = hosts
        self.cloud = cloud
        self.storageroot = storageroot
        self.networks = networks
        self.sublocations = sublocations 
