from core.agility.common.AgilityModelBase import AgilityModelBase

class InterfaceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, macaddress=None, vpcid=None, description=None, instancestatus=None, instanceid=None, networkinterfaceid=None, primaryipaddress=None, location=None, subnetid=None, secondaryipaddress=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'macAddress': {'type': 'string', 'name': 'macaddress', 'minOccurs': '0', 'native': True}, 'vpcId': {'type': 'string', 'name': 'vpcid', 'minOccurs': '0', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}, 'instanceStatus': {'type': 'string', 'name': 'instancestatus', 'minOccurs': '0', 'native': True}, 'instanceId': {'type': 'string', 'name': 'instanceid', 'minOccurs': '0', 'native': True}, 'networkInterfaceId': {'type': 'string', 'name': 'networkinterfaceid', 'minOccurs': '0', 'native': True}, 'primaryIpAddress': {'type': 'string', 'name': 'primaryipaddress', 'minOccurs': '0', 'native': True}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}, 'subnetId': {'type': 'string', 'name': 'subnetid', 'minOccurs': '0', 'native': True}, 'secondaryIpAddress': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'secondaryipaddress', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.macaddress = macaddress
        self.vpcid = vpcid
        self.description = description
        self.instancestatus = instancestatus
        self.instanceid = instanceid
        self.networkinterfaceid = networkinterfaceid
        self.primaryipaddress = primaryipaddress
        self.location = location
        self.subnetid = subnetid
        self.secondaryipaddress = secondaryipaddress 
