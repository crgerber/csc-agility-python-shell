from core.agility.common.AgilityModelBase import AgilityModelBase

class ScriptVariableRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, templateid=None, cloudid=[], topologyid=None, packageid=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'templateId': {'name': 'templateid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'cloudId': {'name': 'cloudid', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'int'}, 'topologyId': {'name': 'topologyid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'packageId': {'name': 'packageid', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'int'}})
        self.templateid = templateid
        self.cloudid = cloudid
        self.topologyid = topologyid
        self.packageid = packageid 
