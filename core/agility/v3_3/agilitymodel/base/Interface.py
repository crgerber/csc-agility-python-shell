from core.agility.common.AgilityModelBase import AgilityModelBase

class InterfaceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, description=None, subnetid=None, primaryipaddress=None, location=None, instanceid=None, instancestatus=None, macaddress=None, secondaryipaddress=[], networkinterfaceid=None, vpcid=None, status=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'name': 'description', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'subnetId': {'name': 'subnetid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'location': {'name': 'location', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'secondaryIpAddress': {'name': 'secondaryipaddress', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'primaryIpAddress': {'name': 'primaryipaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'macAddress': {'name': 'macaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networkInterfaceId': {'name': 'networkinterfaceid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'instanceStatus': {'name': 'instancestatus', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'vpcId': {'name': 'vpcid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'instanceId': {'name': 'instanceid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.description = description
        self.subnetid = subnetid
        self.primaryipaddress = primaryipaddress
        self.location = location
        self.instanceid = instanceid
        self.instancestatus = instancestatus
        self.macaddress = macaddress
        self.secondaryipaddress = secondaryipaddress
        self.networkinterfaceid = networkinterfaceid
        self.vpcid = vpcid
        self.status = status 
