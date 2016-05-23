from core.agility.common.AgilityModelBase import AgilityModelBase

class StoreProductAdapterItemBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', id=None, link=[], type='', resource=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'name': 'description', 'native': True, 'type': 'string'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'link': {'name': 'link', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}, 'resource': {'name': 'resource', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreResource'}})
        self.name = name
        self.description = description
        self.id = id
        self.link = link
        self.type = type
        self.resource = resource 
