from core.agility.common.AgilityModelBase import AgilityModelBase

class PlanEvalRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, loglevel=None, templateid=None, additionalpolicyid=[], ignorerequiredproperties=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'logLevel': {'native': True, 'name': 'loglevel', 'minOccurs': '0', 'type': 'int'}, 'templateId': {'native': True, 'name': 'templateid', 'minOccurs': '0', 'type': 'int'}, 'additionalPolicyId': {'maxOccurs': 'unbounded', 'native': True, 'name': 'additionalpolicyid', 'minOccurs': '0', 'type': 'int'}, 'ignoreRequiredProperties': {'native': True, 'name': 'ignorerequiredproperties', 'type': 'boolean'}})
        self.loglevel = loglevel
        self.templateid = templateid
        self.additionalpolicyid = additionalpolicyid
        self.ignorerequiredproperties = ignorerequiredproperties 
