from core.agility.v3_3.agilitymodel.base.ServiceProvider import ServiceProviderBase

class NetworkServiceBase(ServiceProviderBase):
    '''
    classdocs
    '''
    def __init__(self):
        ServiceProviderBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
