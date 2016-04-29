from core.agility.common.AgilityModelBase import AgilityModelBase

class AttachmentLocationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path='', repository=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'native': True, 'name': 'path', 'type': 'string'}, 'repository': {'native': False, 'name': 'repository', 'type': 'Link'}})
        self.path = path
        self.repository = repository 
