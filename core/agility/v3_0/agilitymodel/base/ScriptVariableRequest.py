from core.agility.common.AgilityModelBase import AgilityModelBase


class ScriptVariableRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, topologyid=None, cloudid=[], packageid=[], templateid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'topologyId': {'type': 'int', 'name': 'topologyid', 'minOccurs': '0', 'native': True}, 'cloudId': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'cloudid', 'minOccurs': '0', 'native': True}, 'packageId': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'packageid', 'minOccurs': '0', 'native': True}, 'templateId': {'type': 'int', 'name': 'templateid', 'minOccurs': '0', 'native': True}})
        self.topologyid = topologyid
        self.cloudid = cloudid
        self.packageid = packageid
        self.templateid = templateid 
