from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class LocationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, repositories=[], sublocations=[], parentlocation=None, storageroot=None, networks=[], visible=None, properties=[], cloud=None, hosts=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'repositories': {'maxOccurs': 'unbounded', 'native': False, 'name': 'repositories', 'minOccurs': '0', 'type': 'Link'}, 'sublocations': {'maxOccurs': 'unbounded', 'native': False, 'name': 'sublocations', 'minOccurs': '0', 'type': 'Link'}, 'hosts': {'maxOccurs': 'unbounded', 'native': False, 'name': 'hosts', 'minOccurs': '0', 'type': 'Host'}, 'parentLocation': {'native': False, 'name': 'parentlocation', 'minOccurs': '0', 'type': 'Link'}, 'networks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networks', 'minOccurs': '0', 'type': 'Link'}, 'storageRoot': {'native': True, 'name': 'storageroot', 'minOccurs': '0', 'type': 'boolean'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'visible': {'native': True, 'name': 'visible', 'minOccurs': '0', 'type': 'boolean'}})
        self.repositories = repositories
        self.sublocations = sublocations
        self.parentlocation = parentlocation
        self.storageroot = storageroot
        self.networks = networks
        self.visible = visible
        self.properties = properties
        self.cloud = cloud
        self.hosts = hosts 
