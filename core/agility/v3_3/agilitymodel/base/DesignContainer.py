from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class DesignContainerBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, antiaffinity=None, resourceaffinity=None, fixedorderitem=[], deep=False, anyorderitem=[], manualorderitem=[], deployers=[], mandatoryaffinity=None, launcheraccessuri=[], aliases=[]):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'antiAffinity': {'type': 'boolean', 'name': 'antiaffinity', 'minOccurs': '0', 'native': True}, 'resourceAffinity': {'type': 'ResourceAffinity', 'name': 'resourceaffinity', 'native': False}, 'fixedOrderItem': {'maxOccurs': 'unbounded', 'type': 'DesignItem', 'name': 'fixedorderitem', 'minOccurs': '0', 'native': False}, 'deep': {'type': 'boolean', 'name': 'deep', 'native': True}, 'anyOrderItem': {'maxOccurs': 'unbounded', 'type': 'DesignItem', 'name': 'anyorderitem', 'minOccurs': '0', 'native': False}, 'manualOrderItem': {'maxOccurs': 'unbounded', 'type': 'DesignItem', 'name': 'manualorderitem', 'minOccurs': '0', 'native': False}, 'deployers': {'maxOccurs': 'unbounded', 'type': 'DesignDeployer', 'name': 'deployers', 'minOccurs': '0', 'native': False}, 'mandatoryAffinity': {'type': 'boolean', 'name': 'mandatoryaffinity', 'minOccurs': '0', 'native': True}, 'launcherAccessUri': {'maxOccurs': 'unbounded', 'type': 'AccessUri', 'name': 'launcheraccessuri', 'minOccurs': '0', 'native': False}, 'aliases': {'maxOccurs': 'unbounded', 'type': 'DesignAlias', 'name': 'aliases', 'minOccurs': '0', 'native': False}})
        self.antiaffinity = antiaffinity
        self.resourceaffinity = resourceaffinity
        self.fixedorderitem = fixedorderitem
        self.deep = deep
        self.anyorderitem = anyorderitem
        self.manualorderitem = manualorderitem
        self.deployers = deployers
        self.mandatoryaffinity = mandatoryaffinity
        self.launcheraccessuri = launcheraccessuri
        self.aliases = aliases 
