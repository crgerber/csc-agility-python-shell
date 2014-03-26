from core.agility.common.AgilityModelBase import AgilityModelBase


class PlanEvalRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, loglevel=None, additionalpolicyid=[], ignorerequiredproperties=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'logLevel': {'type': 'int', 'name': 'loglevel', 'minOccurs': '0', 'native': True}, 'additionalPolicyId': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'additionalpolicyid', 'minOccurs': '0', 'native': True}, 'ignoreRequiredProperties': {'type': 'boolean', 'name': 'ignorerequiredproperties', 'native': True}})
        self.loglevel = loglevel
        self.additionalpolicyid = additionalpolicyid
        self.ignorerequiredproperties = ignorerequiredproperties 
