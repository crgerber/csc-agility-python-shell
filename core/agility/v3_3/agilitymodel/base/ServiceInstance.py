from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceInstanceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, starttime=None, instanceid='', srcconnections=[], provider=None, stoptime=None, configuration=[], dependent=[], dependency=[], state=None, variables=[], firewallrule=[], destconnections=[], service=None, laststartedorstoppedbyuser=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'startTime': {'name': 'starttime', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'instanceId': {'name': 'instanceid', 'native': True, 'type': 'string'}, 'srcConnections': {'name': 'srcconnections', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'provider': {'name': 'provider', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'stopTime': {'name': 'stoptime', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'configuration': {'name': 'configuration', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'dependent': {'name': 'dependent', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'dependency': {'name': 'dependency', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'state': {'name': 'state', 'native': False, 'type': 'ServiceState'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'firewallRule': {'name': 'firewallrule', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessList'}, 'destConnections': {'name': 'destconnections', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'service': {'name': 'service', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'lastStartedOrStoppedByUser': {'name': 'laststartedorstoppedbyuser', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.starttime = starttime
        self.instanceid = instanceid
        self.srcconnections = srcconnections
        self.provider = provider
        self.stoptime = stoptime
        self.configuration = configuration
        self.dependent = dependent
        self.dependency = dependency
        self.state = state
        self.variables = variables
        self.firewallrule = firewallrule
        self.destconnections = destconnections
        self.service = service
        self.laststartedorstoppedbyuser = laststartedorstoppedbyuser 
