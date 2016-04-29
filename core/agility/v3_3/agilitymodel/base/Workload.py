from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class WorkloadBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, destconnections=None, volumes=[], configurations=[], releasedisks=None, scaleuppolicy=None, resources=[], hostnameprefix=None, basestack=None, scaledownpolicy=None, operatingsystem=None, packages=[], srcconnections=None):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numInstances': {'native': True, 'name': 'numinstances', 'type': 'int'}, 'destConnections': {'native': False, 'name': 'destconnections', 'minOccurs': '0', 'type': 'Link'}, 'releaseDisks': {'native': True, 'name': 'releasedisks', 'minOccurs': '0', 'type': 'boolean'}, 'configurations': {'maxOccurs': 'unbounded', 'native': False, 'name': 'configurations', 'minOccurs': '0', 'type': 'Link'}, 'scaleUpPolicy': {'native': False, 'name': 'scaleuppolicy', 'minOccurs': '0', 'type': 'Policy'}, 'volumes': {'maxOccurs': 'unbounded', 'native': False, 'name': 'volumes', 'minOccurs': '0', 'type': 'Volume'}, 'hostnamePrefix': {'native': True, 'name': 'hostnameprefix', 'minOccurs': '0', 'type': 'string'}, 'baseStack': {'native': False, 'name': 'basestack', 'minOccurs': '0', 'type': 'Link'}, 'scaleDownPolicy': {'native': False, 'name': 'scaledownpolicy', 'minOccurs': '0', 'type': 'Policy'}, 'operatingSystem': {'native': True, 'name': 'operatingsystem', 'minOccurs': '0', 'type': 'string'}, 'packages': {'maxOccurs': 'unbounded', 'native': False, 'name': 'packages', 'minOccurs': '0', 'type': 'Link'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'Resource'}, 'srcConnections': {'native': False, 'name': 'srcconnections', 'minOccurs': '0', 'type': 'Link'}})
        self.numinstances = numinstances
        self.destconnections = destconnections
        self.volumes = volumes
        self.configurations = configurations
        self.releasedisks = releasedisks
        self.scaleuppolicy = scaleuppolicy
        self.resources = resources
        self.hostnameprefix = hostnameprefix
        self.basestack = basestack
        self.scaledownpolicy = scaledownpolicy
        self.operatingsystem = operatingsystem
        self.packages = packages
        self.srcconnections = srcconnections 
