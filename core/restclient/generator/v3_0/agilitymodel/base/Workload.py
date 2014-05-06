from DesignItem import DesignItemBase

class WorkloadBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, releasedisks=None, numinstances=None, scaleuppolicy=None, scaledownpolicy=None, srcconnections=None, hostnameprefix=None, volumes=[], destconnections=None, packages=[], basestack=None, operatingsystem=None, resources=[], configurations=[]):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'releaseDisks': {'type': 'boolean', 'name': 'releasedisks', 'minOccurs': '0', 'native': True}, 'numInstances': {'type': 'int', 'name': 'numinstances', 'native': True}, 'volumes': {'maxOccurs': 'unbounded', 'type': 'Volume', 'name': 'volumes', 'minOccurs': '0', 'native': False}, 'scaleDownPolicy': {'type': 'Policy', 'name': 'scaledownpolicy', 'minOccurs': '0', 'native': False}, 'srcConnections': {'type': 'Link', 'name': 'srcconnections', 'minOccurs': '0', 'native': False}, 'hostnamePrefix': {'type': 'string', 'name': 'hostnameprefix', 'minOccurs': '0', 'native': True}, 'scaleUpPolicy': {'type': 'Policy', 'name': 'scaleuppolicy', 'minOccurs': '0', 'native': False}, 'destConnections': {'type': 'Link', 'name': 'destconnections', 'minOccurs': '0', 'native': False}, 'packages': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'packages', 'minOccurs': '0', 'native': False}, 'baseStack': {'type': 'Link', 'name': 'basestack', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'type': 'string', 'name': 'operatingsystem', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'configurations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'configurations', 'minOccurs': '0', 'native': False}})
        self.releasedisks = releasedisks
        self.numinstances = numinstances
        self.scaleuppolicy = scaleuppolicy
        self.scaledownpolicy = scaledownpolicy
        self.srcconnections = srcconnections
        self.hostnameprefix = hostnameprefix
        self.volumes = volumes
        self.destconnections = destconnections
        self.packages = packages
        self.basestack = basestack
        self.operatingsystem = operatingsystem
        self.resources = resources
        self.configurations = configurations 
