from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class WorkflowRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, comment=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'comment': {'type': 'string', 'name': 'comment', 'minOccurs': '0', 'native': True}})
        self.comment = comment 
