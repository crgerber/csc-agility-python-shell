from core.agility.v3_3.agilitymodel.base.PolicyMeta import PolicyMetaBase

class WorkflowPolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
