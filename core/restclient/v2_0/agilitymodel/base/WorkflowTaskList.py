from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class WorkflowTaskListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, totalCount=None, tasks=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'type': 'int', 'name': 'totalCount', 'native': True}, 'tasks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'tasks', 'minOccurs': '0', 'native': False}})
        self.totalCount = totalCount
        self.tasks = tasks 
