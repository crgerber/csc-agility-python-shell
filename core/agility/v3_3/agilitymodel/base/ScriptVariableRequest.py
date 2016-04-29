from core.agility.common.AgilityModelBase import AgilityModelBase

class ScriptVariableRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, templateid=None, packageid=[], topologyid=None, cloudid=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'templateId': {'native': True, 'name': 'templateid', 'minOccurs': '0', 'type': 'int'}, 'packageId': {'maxOccurs': 'unbounded', 'native': True, 'name': 'packageid', 'minOccurs': '0', 'type': 'int'}, 'topologyId': {'native': True, 'name': 'topologyid', 'minOccurs': '0', 'type': 'int'}, 'cloudId': {'maxOccurs': 'unbounded', 'native': True, 'name': 'cloudid', 'minOccurs': '0', 'type': 'int'}})
        self.templateid = templateid
        self.packageid = packageid
        self.topologyid = topologyid
        self.cloudid = cloudid 
