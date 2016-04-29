from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class InstanceVariableRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, instanceid=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instanceId': {'native': True, 'name': 'instanceid', 'type': 'int'}})
        self.instanceid = instanceid 
