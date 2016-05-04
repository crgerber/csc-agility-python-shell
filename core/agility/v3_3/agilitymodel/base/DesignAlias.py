from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DesignAliasBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, workloadlogicalid=None, workloadid=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'workloadId': {'type': 'int', 'name': 'workloadid', 'minOccurs': '0', 'native': True}, 'workloadLogicalId': {'type': 'string', 'name': 'workloadlogicalid', 'minOccurs': '0', 'native': True}})
        self.workloadlogicalid = workloadlogicalid
        self.workloadid = workloadid 
