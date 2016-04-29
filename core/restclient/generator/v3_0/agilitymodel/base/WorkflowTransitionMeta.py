from .AgilityModelBase import AgilityModelBase

class WorkflowTransitionMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', skipvalidation=False, formname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'type': 'string', 'name': 'name', 'native': True}, 'skipValidation': {'type': 'boolean', 'name': 'skipvalidation', 'native': True}, 'formName': {'type': 'string', 'name': 'formname', 'native': True}})
        self.name = name
        self.skipvalidation = skipvalidation
        self.formname = formname 
