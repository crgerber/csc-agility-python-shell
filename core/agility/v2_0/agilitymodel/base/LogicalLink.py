from core.agility.v2_0.agilitymodel.base.Link import LinkBase

class LogicalLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, logicalId=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'logicalId': {'type': 'string', 'name': 'logicalId', 'minOccurs': '0', 'native': True}})
        self.logicalId = logicalId 
