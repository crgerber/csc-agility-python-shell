from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, comment=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'comment': {'name': 'comment', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.comment = comment 
