from core.restclient.v2_0.agilitymodel.base.DesignItem import DesignItemBase

class DesignContainerBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, antiAffinity=None, resourceAffinity=None, fixedOrderItem=list(), deep=False, anyOrderItem=list(), manualOrderItem=list(), deployers=list(), mandatoryAffinity=None, launcherAccessUri=list(), aliases=list()):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'antiAffinity': {'type': 'boolean', 'name': 'antiAffinity', 'minOccurs': '0', 'native': True}, 'resourceAffinity': {'type': 'ResourceAffinity', 'name': 'resourceAffinity', 'native': False}, 'fixedOrderItem': {'maxOccurs': 'unbounded', 'type': 'DesignItem', 'name': 'fixedOrderItem', 'minOccurs': '0', 'native': False}, 'deep': {'type': 'boolean', 'name': 'deep', 'native': True}, 'anyOrderItem': {'maxOccurs': 'unbounded', 'type': 'DesignItem', 'name': 'anyOrderItem', 'minOccurs': '0', 'native': False}, 'manualOrderItem': {'maxOccurs': 'unbounded', 'type': 'DesignItem', 'name': 'manualOrderItem', 'minOccurs': '0', 'native': False}, 'deployers': {'maxOccurs': 'unbounded', 'type': 'DesignDeployer', 'name': 'deployers', 'minOccurs': '0', 'native': False}, 'mandatoryAffinity': {'type': 'boolean', 'name': 'mandatoryAffinity', 'minOccurs': '0', 'native': True}, 'launcherAccessUri': {'maxOccurs': 'unbounded', 'type': 'AccessUri', 'name': 'launcherAccessUri', 'minOccurs': '0', 'native': False}, 'aliases': {'maxOccurs': 'unbounded', 'type': 'DesignAlias', 'name': 'aliases', 'minOccurs': '0', 'native': False}})
        self.antiAffinity = antiAffinity
        self.resourceAffinity = resourceAffinity
        self.fixedOrderItem = fixedOrderItem
        self.deep = deep
        self.anyOrderItem = anyOrderItem
        self.manualOrderItem = manualOrderItem
        self.deployers = deployers
        self.mandatoryAffinity = mandatoryAffinity
        self.launcherAccessUri = launcherAccessUri
        self.aliases = aliases 
