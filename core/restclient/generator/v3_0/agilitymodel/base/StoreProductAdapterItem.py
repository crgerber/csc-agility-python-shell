from AgilityModelBase import AgilityModelBase

class StoreProductAdapterItemBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resource=[], description='', link=[], type='', id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resource': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resource', 'minOccurs': '0', 'native': False}, 'description': {'type': 'string', 'name': 'description', 'native': True}, 'link': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'link', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.resource = resource
        self.description = description
        self.link = link
        self.type = type
        self.id = id
        self.name = name 
