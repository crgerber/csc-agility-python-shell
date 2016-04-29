from core.agility.common.AgilityModelBase import AgilityModelBase

class StoreProductAdapterItemBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resource=[], description='', link=[], name='', id=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resource': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resource', 'minOccurs': '0', 'type': 'StoreResource'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'link': {'maxOccurs': 'unbounded', 'native': False, 'name': 'link', 'minOccurs': '0', 'type': 'Link'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.resource = resource
        self.description = description
        self.link = link
        self.name = name
        self.id = id
        self.type = type 
