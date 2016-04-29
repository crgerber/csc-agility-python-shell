from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class DesignContainerBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, resourceaffinity=None, launcheraccessuri=[], anyorderitem=[], deep=False, antiaffinity=None, mandatoryaffinity=None, manualorderitem=[], aliases=[], deployers=[], fixedorderitem=[]):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceAffinity': {'native': False, 'name': 'resourceaffinity', 'type': 'ResourceAffinity'}, 'deployers': {'maxOccurs': 'unbounded', 'native': False, 'name': 'deployers', 'minOccurs': '0', 'type': 'DesignDeployer'}, 'antiAffinity': {'native': True, 'name': 'antiaffinity', 'minOccurs': '0', 'type': 'boolean'}, 'fixedOrderItem': {'maxOccurs': 'unbounded', 'native': False, 'name': 'fixedorderitem', 'minOccurs': '0', 'type': 'DesignItem'}, 'launcherAccessUri': {'maxOccurs': 'unbounded', 'native': False, 'name': 'launcheraccessuri', 'minOccurs': '0', 'type': 'AccessUri'}, 'anyOrderItem': {'maxOccurs': 'unbounded', 'native': False, 'name': 'anyorderitem', 'minOccurs': '0', 'type': 'DesignItem'}, 'manualOrderItem': {'maxOccurs': 'unbounded', 'native': False, 'name': 'manualorderitem', 'minOccurs': '0', 'type': 'DesignItem'}, 'mandatoryAffinity': {'native': True, 'name': 'mandatoryaffinity', 'minOccurs': '0', 'type': 'boolean'}, 'aliases': {'maxOccurs': 'unbounded', 'native': False, 'name': 'aliases', 'minOccurs': '0', 'type': 'DesignAlias'}, 'deep': {'native': True, 'name': 'deep', 'type': 'boolean'}})
        self.resourceaffinity = resourceaffinity
        self.launcheraccessuri = launcheraccessuri
        self.anyorderitem = anyorderitem
        self.deep = deep
        self.antiaffinity = antiaffinity
        self.mandatoryaffinity = mandatoryaffinity
        self.manualorderitem = manualorderitem
        self.aliases = aliases
        self.deployers = deployers
        self.fixedorderitem = fixedorderitem 
