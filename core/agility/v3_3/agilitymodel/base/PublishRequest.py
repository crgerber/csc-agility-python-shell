from core.agility.common.AgilityModelBase import AgilityModelBase

class PublishRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, comment=None, keepsubassetslocation=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'keepSubAssetsLocation': {'name': 'keepsubassetslocation', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'comment': {'name': 'comment', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.comment = comment
        self.keepsubassetslocation = keepsubassetslocation 
