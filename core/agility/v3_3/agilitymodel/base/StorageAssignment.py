from core.agility.common.AgilityModelBase import AgilityModelBase

class StorageAssignmentBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, attachtime=None, device=None, instanceid=None, status=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'attachTime': {'native': True, 'name': 'attachtime', 'minOccurs': '0', 'type': 'dateTime'}, 'device': {'native': True, 'name': 'device', 'minOccurs': '0', 'type': 'string'}, 'instanceId': {'native': True, 'name': 'instanceid', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}})
        self.attachtime = attachtime
        self.device = device
        self.instanceid = instanceid
        self.status = status 
