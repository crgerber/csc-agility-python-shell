from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class DesignConnectionBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, srcid=None, destid=None, srclogicalid=None, destlogicalid=None):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'srcId': {'name': 'srcid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'destId': {'name': 'destid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'srcLogicalId': {'name': 'srclogicalid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'destLogicalId': {'name': 'destlogicalid', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.srcid = srcid
        self.destid = destid
        self.srclogicalid = srclogicalid
        self.destlogicalid = destlogicalid 
