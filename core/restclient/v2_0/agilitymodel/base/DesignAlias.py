from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class DesignAliasBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, workloadLogicalId=None, workloadId=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'workloadId': {'type': 'int', 'name': 'workloadId', 'minOccurs': '0', 'native': True}, 'workloadLogicalId': {'type': 'string', 'name': 'workloadLogicalId', 'minOccurs': '0', 'native': True}})
        self.workloadLogicalId = workloadLogicalId
        self.workloadId = workloadId 
