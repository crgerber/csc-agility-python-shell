from core.agility.common.AgilityModelBase import AgilityModelBase

class StorageAssignmentBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, attachtime=None, device=None, instanceid=None, status=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attachTime': {'name': 'attachtime', 'minOccurs': '0', 'native': True, 'type': 'dateTime'}, 'device': {'name': 'device', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'instanceId': {'name': 'instanceid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.attachtime = attachtime
        self.device = device
        self.instanceid = instanceid
        self.status = status 
