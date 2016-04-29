from core.agility.common.AgilityModelBase import AgilityModelBase

class InterfaceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, networkinterfaceid=None, vpcid=None, subnetid=None, secondaryipaddress=[], primaryipaddress=None, description=None, location=None, macaddress=None, instanceid=None, status=None, instancestatus=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkInterfaceId': {'native': True, 'name': 'networkinterfaceid', 'minOccurs': '0', 'type': 'string'}, 'vpcId': {'native': True, 'name': 'vpcid', 'minOccurs': '0', 'type': 'string'}, 'subnetId': {'native': True, 'name': 'subnetid', 'minOccurs': '0', 'type': 'string'}, 'instanceStatus': {'native': True, 'name': 'instancestatus', 'minOccurs': '0', 'type': 'string'}, 'secondaryIpAddress': {'maxOccurs': 'unbounded', 'native': True, 'name': 'secondaryipaddress', 'minOccurs': '0', 'type': 'string'}, 'description': {'native': True, 'name': 'description', 'minOccurs': '0', 'type': 'string'}, 'location': {'native': True, 'name': 'location', 'minOccurs': '0', 'type': 'string'}, 'macAddress': {'native': True, 'name': 'macaddress', 'minOccurs': '0', 'type': 'string'}, 'instanceId': {'native': True, 'name': 'instanceid', 'minOccurs': '0', 'type': 'string'}, 'primaryIpAddress': {'native': True, 'name': 'primaryipaddress', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}})
        self.networkinterfaceid = networkinterfaceid
        self.vpcid = vpcid
        self.subnetid = subnetid
        self.secondaryipaddress = secondaryipaddress
        self.primaryipaddress = primaryipaddress
        self.description = description
        self.location = location
        self.macaddress = macaddress
        self.instanceid = instanceid
        self.status = status
        self.instancestatus = instancestatus 
