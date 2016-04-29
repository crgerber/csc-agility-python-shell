from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class DesignConnectionBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, destlogicalid=None, destid=None, srclogicalid=None, srcid=None):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'destLogicalId': {'native': True, 'name': 'destlogicalid', 'minOccurs': '0', 'type': 'string'}, 'srcId': {'native': True, 'name': 'srcid', 'minOccurs': '0', 'type': 'int'}, 'srcLogicalId': {'native': True, 'name': 'srclogicalid', 'minOccurs': '0', 'type': 'string'}, 'destId': {'native': True, 'name': 'destid', 'minOccurs': '0', 'type': 'int'}})
        self.destlogicalid = destlogicalid
        self.destid = destid
        self.srclogicalid = srclogicalid
        self.srcid = srcid 
