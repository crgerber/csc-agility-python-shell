from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DesignAliasBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, workloadid=None, workloadlogicalid=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'workloadId': {'name': 'workloadid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'workloadLogicalId': {'name': 'workloadlogicalid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.workloadid = workloadid
        self.workloadlogicalid = workloadlogicalid 
