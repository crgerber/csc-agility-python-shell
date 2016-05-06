from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase

class ServiceBase(DesignItemBase):
    '''
    classdocs
    '''
    def __init__(self):
        DesignItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
