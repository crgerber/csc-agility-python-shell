from core.agility.v3_0.agilitymodel.base.DesignItem import DesignItemBase

class DesignConnectionBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, srclogicalid=None, destlogicalid=None, srcid=None, destid=None):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'srcLogicalId': {'type': 'string', 'name': 'srclogicalid', 'minOccurs': '0', 'native': True}, 'destLogicalId': {'type': 'string', 'name': 'destlogicalid', 'minOccurs': '0', 'native': True}, 'srcId': {'type': 'int', 'name': 'srcid', 'minOccurs': '0', 'native': True}, 'destId': {'type': 'int', 'name': 'destid', 'minOccurs': '0', 'native': True}})
        self.srclogicalid = srclogicalid
        self.destlogicalid = destlogicalid
        self.srcid = srcid
        self.destid = destid 
