from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class DesignContainerBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, anyorderitem=[], antiaffinity=None, deep=False, manualorderitem=[], fixedorderitem=[], resourceaffinity=None, mandatoryaffinity=None, aliases=[], deployers=[], launcheraccessuri=[]):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'anyOrderItem': {'name': 'anyorderitem', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DesignItem'}, 'antiAffinity': {'name': 'antiaffinity', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'deep': {'name': 'deep', 'native': True, 'type': 'boolean'}, 'manualOrderItem': {'name': 'manualorderitem', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DesignItem'}, 'aliases': {'name': 'aliases', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DesignAlias'}, 'resourceAffinity': {'name': 'resourceaffinity', 'native': False, 'type': 'ResourceAffinity'}, 'mandatoryAffinity': {'name': 'mandatoryaffinity', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'fixedOrderItem': {'name': 'fixedorderitem', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DesignItem'}, 'deployers': {'name': 'deployers', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DesignDeployer'}, 'launcherAccessUri': {'name': 'launcheraccessuri', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessUri'}})
        self.anyorderitem = anyorderitem
        self.antiaffinity = antiaffinity
        self.deep = deep
        self.manualorderitem = manualorderitem
        self.fixedorderitem = fixedorderitem
        self.resourceaffinity = resourceaffinity
        self.mandatoryaffinity = mandatoryaffinity
        self.aliases = aliases
        self.deployers = deployers
        self.launcheraccessuri = launcheraccessuri 
