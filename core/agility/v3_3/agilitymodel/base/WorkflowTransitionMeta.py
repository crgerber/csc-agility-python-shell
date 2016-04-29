from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTransitionMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, skipvalidation=False, name='', formname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'skipValidation': {'native': True, 'name': 'skipvalidation', 'type': 'boolean'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'formName': {'native': True, 'name': 'formname', 'type': 'string'}})
        self.skipvalidation = skipvalidation
        self.name = name
        self.formname = formname 
