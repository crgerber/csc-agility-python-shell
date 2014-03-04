from core.restclient.v2_0.agilitymodel.base.DesignItem import DesignItemBase

class WorkloadBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, numInstances=None, scaleUpPolicy=None, scaleDownPolicy=None, srcConnections=None, hostnamePrefix=None, volumes=list(), destConnections=None, packages=list(), baseStack=None, operatingSystem=None, resources=list(), configurations=list()):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numInstances': {'type': 'int', 'name': 'numInstances', 'native': True}, 'scaleUpPolicy': {'type': 'Policy', 'name': 'scaleUpPolicy', 'minOccurs': '0', 'native': False}, 'scaleDownPolicy': {'type': 'Policy', 'name': 'scaleDownPolicy', 'minOccurs': '0', 'native': False}, 'srcConnections': {'type': 'Link', 'name': 'srcConnections', 'minOccurs': '0', 'native': False}, 'hostnamePrefix': {'type': 'string', 'name': 'hostnamePrefix', 'minOccurs': '0', 'native': True}, 'volumes': {'maxOccurs': 'unbounded', 'type': 'Volume', 'name': 'volumes', 'minOccurs': '0', 'native': False}, 'destConnections': {'type': 'Link', 'name': 'destConnections', 'minOccurs': '0', 'native': False}, 'packages': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'packages', 'minOccurs': '0', 'native': False}, 'baseStack': {'type': 'Link', 'name': 'baseStack', 'minOccurs': '0', 'native': False}, 'operatingSystem': {'type': 'string', 'name': 'operatingSystem', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'configurations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'configurations', 'minOccurs': '0', 'native': False}})
        self.numInstances = numInstances
        self.scaleUpPolicy = scaleUpPolicy
        self.scaleDownPolicy = scaleDownPolicy
        self.srcConnections = srcConnections
        self.hostnamePrefix = hostnamePrefix
        self.volumes = volumes
        self.destConnections = destConnections
        self.packages = packages
        self.baseStack = baseStack
        self.operatingSystem = operatingSystem
        self.resources = resources
        self.configurations = configurations 
