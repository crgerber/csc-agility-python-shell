from core.agility.common.AgilityModelBase import AgilityModelBase

class PlanEvalRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, templateid=None, loglevel=None, additionalpolicyid=[], ignorerequiredproperties=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'templateId': {'name': 'templateid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'logLevel': {'name': 'loglevel', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'additionalPolicyId': {'name': 'additionalpolicyid', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'int'}, 'ignoreRequiredProperties': {'name': 'ignorerequiredproperties', 'native': True, 'type': 'boolean'}})
        self.templateid = templateid
        self.loglevel = loglevel
        self.additionalpolicyid = additionalpolicyid
        self.ignorerequiredproperties = ignorerequiredproperties 
