from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceInstanceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, laststartedorstoppedbyuser=None, dependent=[], destconnections=[], dependency=[], instanceid='', state=None, provider=None, starttime=None, configuration=[], srcconnections=[], service=None, stoptime=None, firewallrule=[], variables=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'lastStartedOrStoppedByUser': {'native': False, 'name': 'laststartedorstoppedbyuser', 'minOccurs': '0', 'type': 'Link'}, 'dependent': {'maxOccurs': 'unbounded', 'native': False, 'name': 'dependent', 'minOccurs': '0', 'type': 'Link'}, 'dependency': {'maxOccurs': 'unbounded', 'native': False, 'name': 'dependency', 'minOccurs': '0', 'type': 'Link'}, 'destConnections': {'maxOccurs': 'unbounded', 'native': False, 'name': 'destconnections', 'minOccurs': '0', 'type': 'Link'}, 'instanceId': {'native': True, 'name': 'instanceid', 'type': 'string'}, 'state': {'native': False, 'name': 'state', 'type': 'ServiceState'}, 'provider': {'native': False, 'name': 'provider', 'minOccurs': '0', 'type': 'Link'}, 'startTime': {'native': True, 'name': 'starttime', 'minOccurs': '0', 'type': 'date'}, 'configuration': {'maxOccurs': 'unbounded', 'native': False, 'name': 'configuration', 'minOccurs': '0', 'type': 'AssetProperty'}, 'srcConnections': {'maxOccurs': 'unbounded', 'native': False, 'name': 'srcconnections', 'minOccurs': '0', 'type': 'Link'}, 'service': {'native': False, 'name': 'service', 'minOccurs': '0', 'type': 'Link'}, 'stopTime': {'native': True, 'name': 'stoptime', 'minOccurs': '0', 'type': 'date'}, 'firewallRule': {'maxOccurs': 'unbounded', 'native': False, 'name': 'firewallrule', 'minOccurs': '0', 'type': 'AccessList'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.laststartedorstoppedbyuser = laststartedorstoppedbyuser
        self.dependent = dependent
        self.destconnections = destconnections
        self.dependency = dependency
        self.instanceid = instanceid
        self.state = state
        self.provider = provider
        self.starttime = starttime
        self.configuration = configuration
        self.srcconnections = srcconnections
        self.service = service
        self.stoptime = stoptime
        self.firewallrule = firewallrule
        self.variables = variables 
