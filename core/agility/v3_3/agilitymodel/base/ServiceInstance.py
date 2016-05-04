from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceInstanceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, service=None, firewallrule=[], dependency=[], instanceid='', variables=[], srcconnections=[], dependent=[], state=None, stoptime=None, starttime=None, provider=None, destconnections=[], configuration=[], laststartedorstoppedbyuser=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'service': {'type': 'Link', 'name': 'service', 'minOccurs': '0', 'native': False}, 'firewallRule': {'maxOccurs': 'unbounded', 'type': 'AccessList', 'name': 'firewallrule', 'minOccurs': '0', 'native': False}, 'instanceId': {'type': 'string', 'name': 'instanceid', 'native': True}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'destConnections': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'destconnections', 'minOccurs': '0', 'native': False}, 'srcConnections': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'srcconnections', 'minOccurs': '0', 'native': False}, 'dependency': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'dependency', 'minOccurs': '0', 'native': False}, 'state': {'type': 'ServiceState', 'name': 'state', 'native': False}, 'stopTime': {'type': 'date', 'name': 'stoptime', 'minOccurs': '0', 'native': True}, 'startTime': {'type': 'date', 'name': 'starttime', 'minOccurs': '0', 'native': True}, 'provider': {'type': 'Link', 'name': 'provider', 'minOccurs': '0', 'native': False}, 'dependent': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'dependent', 'minOccurs': '0', 'native': False}, 'configuration': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'configuration', 'minOccurs': '0', 'native': False}, 'lastStartedOrStoppedByUser': {'type': 'Link', 'name': 'laststartedorstoppedbyuser', 'minOccurs': '0', 'native': False}})
        self.service = service
        self.firewallrule = firewallrule
        self.dependency = dependency
        self.instanceid = instanceid
        self.variables = variables
        self.srcconnections = srcconnections
        self.dependent = dependent
        self.state = state
        self.stoptime = stoptime
        self.starttime = starttime
        self.provider = provider
        self.destconnections = destconnections
        self.configuration = configuration
        self.laststartedorstoppedbyuser = laststartedorstoppedbyuser 
