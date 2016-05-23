from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentPlanBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, message='', rank=None, stackdefault=False, option=[], name='', resourceaffinity=None, resource=[], child=[], error=False, item=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'message': {'name': 'message', 'native': True, 'type': 'string'}, 'rank': {'name': 'rank', 'native': True, 'type': 'double'}, 'item': {'name': 'item', 'native': False, 'type': 'Link'}, 'option': {'name': 'option', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DeploymentPlan'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'resourceAffinity': {'name': 'resourceaffinity', 'native': False, 'type': 'ResourceAffinity'}, 'stackDefault': {'name': 'stackdefault', 'native': True, 'type': 'boolean'}, 'child': {'name': 'child', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DeploymentPlan'}, 'error': {'name': 'error', 'native': True, 'type': 'boolean'}, 'resource': {'name': 'resource', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.message = message
        self.rank = rank
        self.stackdefault = stackdefault
        self.option = option
        self.name = name
        self.resourceaffinity = resourceaffinity
        self.resource = resource
        self.child = child
        self.error = error
        self.item = item 
