from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class CloudPropertyRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, defaultvalue=False, propertyname=''):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'defaultValue': {'name': 'defaultvalue', 'native': True, 'type': 'boolean'}, 'propertyName': {'name': 'propertyname', 'native': True, 'type': 'string'}})
        self.defaultvalue = defaultvalue
        self.propertyname = propertyname 
