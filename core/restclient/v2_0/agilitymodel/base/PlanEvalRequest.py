from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class PlanEvalRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, logLevel=None, additionalPolicyId=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'logLevel': {'type': 'int', 'name': 'logLevel', 'minOccurs': '0', 'native': True}, 'additionalPolicyId': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'additionalPolicyId', 'minOccurs': '0', 'native': True}})
        self.logLevel = logLevel
        self.additionalPolicyId = additionalPolicyId 
