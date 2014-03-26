from core.agility.common.AgilityModelBase import AgilityModelBase


class WorkflowTransitionMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', skipValidation=False, formName=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'type': 'string', 'name': 'name', 'native': True}, 'skipValidation': {'type': 'boolean', 'name': 'skipValidation', 'native': True}, 'formName': {'type': 'string', 'name': 'formName', 'native': True}})
        self.name = name
        self.skipValidation = skipValidation
        self.formName = formName 
