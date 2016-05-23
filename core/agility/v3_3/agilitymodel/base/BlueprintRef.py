from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class BlueprintRefBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self, blueprint=None):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'blueprint': {'name': 'blueprint', 'native': False, 'type': 'Link'}})
        self.blueprint = blueprint 
