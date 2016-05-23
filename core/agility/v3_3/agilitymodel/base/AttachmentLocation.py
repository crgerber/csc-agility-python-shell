from core.agility.common.AgilityModelBase import AgilityModelBase

class AttachmentLocationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path='', repository=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'name': 'path', 'native': True, 'type': 'string'}, 'repository': {'name': 'repository', 'native': False, 'type': 'Link'}})
        self.path = path
        self.repository = repository 
