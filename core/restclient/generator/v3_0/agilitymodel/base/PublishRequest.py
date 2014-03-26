from AgilityModelBase import AgilityModelBase

class PublishRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, comment=None, keepsubassetslocation=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'comment': {'type': 'string', 'name': 'comment', 'minOccurs': '0', 'native': True}, 'keepSubAssetsLocation': {'type': 'boolean', 'name': 'keepsubassetslocation', 'minOccurs': '0', 'native': True}})
        self.comment = comment
        self.keepsubassetslocation = keepsubassetslocation 
