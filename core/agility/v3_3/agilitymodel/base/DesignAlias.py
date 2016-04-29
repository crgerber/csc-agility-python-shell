from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class DesignAliasBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, workloadlogicalid=None, workloadid=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'workloadLogicalId': {'native': True, 'name': 'workloadlogicalid', 'minOccurs': '0', 'type': 'string'}, 'workloadId': {'native': True, 'name': 'workloadid', 'minOccurs': '0', 'type': 'int'}})
        self.workloadlogicalid = workloadlogicalid
        self.workloadid = workloadid 
