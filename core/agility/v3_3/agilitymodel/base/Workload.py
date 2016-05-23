from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class WorkloadBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, hostnameprefix=None, operatingsystem=None, srcconnections=None, destconnections=None, releasedisks=None, basestack=None, numinstances=None, scaleuppolicy=None, scaledownpolicy=None, configurations=[], packages=[], volumes=[], resources=[]):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'hostnamePrefix': {'name': 'hostnameprefix', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'scaleDownPolicy': {'name': 'scaledownpolicy', 'minOccurs': '0', 'native': False, 'type': 'Policy'}, 'srcConnections': {'name': 'srcconnections', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'packages': {'name': 'packages', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'releaseDisks': {'name': 'releasedisks', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'baseStack': {'name': 'basestack', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'numInstances': {'name': 'numinstances', 'native': True, 'type': 'int'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Resource'}, 'operatingSystem': {'name': 'operatingsystem', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'configurations': {'name': 'configurations', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'destConnections': {'name': 'destconnections', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'volumes': {'name': 'volumes', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Volume'}, 'scaleUpPolicy': {'name': 'scaleuppolicy', 'minOccurs': '0', 'native': False, 'type': 'Policy'}})
        self.hostnameprefix = hostnameprefix
        self.operatingsystem = operatingsystem
        self.srcconnections = srcconnections
        self.destconnections = destconnections
        self.releasedisks = releasedisks
        self.basestack = basestack
        self.numinstances = numinstances
        self.scaleuppolicy = scaleuppolicy
        self.scaledownpolicy = scaledownpolicy
        self.configurations = configurations
        self.packages = packages
        self.volumes = volumes
        self.resources = resources 
