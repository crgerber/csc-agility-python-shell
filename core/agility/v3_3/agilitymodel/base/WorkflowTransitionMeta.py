from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTransitionMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', skipvalidation=False, formname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'skipValidation': {'name': 'skipvalidation', 'native': True, 'type': 'boolean'}, 'formName': {'name': 'formname', 'native': True, 'type': 'string'}})
        self.name = name
        self.skipvalidation = skipvalidation
        self.formname = formname 
