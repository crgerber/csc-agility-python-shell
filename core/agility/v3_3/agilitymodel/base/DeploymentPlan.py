from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentPlanBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, resourceaffinity=None, error=False, resource=[], child=[], option=[], item=None, message='', name='', rank=None, stackdefault=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceAffinity': {'native': False, 'name': 'resourceaffinity', 'type': 'ResourceAffinity'}, 'error': {'native': True, 'name': 'error', 'type': 'boolean'}, 'resource': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resource', 'minOccurs': '0', 'type': 'Link'}, 'option': {'maxOccurs': 'unbounded', 'native': False, 'name': 'option', 'minOccurs': '0', 'type': 'DeploymentPlan'}, 'item': {'native': False, 'name': 'item', 'type': 'Link'}, 'message': {'native': True, 'name': 'message', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'child': {'maxOccurs': 'unbounded', 'native': False, 'name': 'child', 'minOccurs': '0', 'type': 'DeploymentPlan'}, 'rank': {'native': True, 'name': 'rank', 'type': 'double'}, 'stackDefault': {'native': True, 'name': 'stackdefault', 'type': 'boolean'}})
        self.resourceaffinity = resourceaffinity
        self.error = error
        self.resource = resource
        self.child = child
        self.option = option
        self.item = item
        self.message = message
        self.name = name
        self.rank = rank
        self.stackdefault = stackdefault 
