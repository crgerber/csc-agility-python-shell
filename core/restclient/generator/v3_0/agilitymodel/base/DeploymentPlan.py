from .AgilityModelBase import AgilityModelBase

class DeploymentPlanBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, stackdefault=False, resource=[], name='', resourceaffinity=None, child=[], rank=None, item=None, error=False, message='', option=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'error': {'type': 'boolean', 'name': 'error', 'native': True}, 'resource': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'resource', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'resourceAffinity': {'type': 'ResourceAffinity', 'name': 'resourceaffinity', 'native': False}, 'stackDefault': {'type': 'boolean', 'name': 'stackdefault', 'native': True}, 'rank': {'type': 'double', 'name': 'rank', 'native': True}, 'item': {'type': 'Link', 'name': 'item', 'native': False}, 'child': {'maxOccurs': 'unbounded', 'type': 'DeploymentPlan', 'name': 'child', 'minOccurs': '0', 'native': False}, 'message': {'type': 'string', 'name': 'message', 'native': True}, 'option': {'maxOccurs': 'unbounded', 'type': 'DeploymentPlan', 'name': 'option', 'minOccurs': '0', 'native': False}})
        self.stackdefault = stackdefault
        self.resource = resource
        self.name = name
        self.resourceaffinity = resourceaffinity
        self.child = child
        self.rank = rank
        self.item = item
        self.error = error
        self.message = message
        self.option = option 
