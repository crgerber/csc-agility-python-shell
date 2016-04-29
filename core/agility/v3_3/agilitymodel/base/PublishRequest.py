from core.agility.common.AgilityModelBase import AgilityModelBase

class PublishRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, comment=None, keepsubassetslocation=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'comment': {'native': True, 'name': 'comment', 'minOccurs': '0', 'type': 'string'}, 'keepSubAssetsLocation': {'native': True, 'name': 'keepsubassetslocation', 'minOccurs': '0', 'type': 'boolean'}})
        self.comment = comment
        self.keepsubassetslocation = keepsubassetslocation 
