from core.agility.common.AgilityModelBase import AgilityModelBase

class StorageAssignmentBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, instanceid=None, device=None, status=None, attachtime=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instanceId': {'type': 'string', 'name': 'instanceid', 'minOccurs': '0', 'native': True}, 'device': {'type': 'string', 'name': 'device', 'minOccurs': '0', 'native': True}, 'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'attachTime': {'type': 'dateTime', 'name': 'attachtime', 'minOccurs': '0', 'native': True}})
        self.instanceid = instanceid
        self.device = device
        self.status = status
        self.attachtime = attachtime 
