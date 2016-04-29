from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class CloudPropertyRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, propertyname='', defaultvalue=False):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'propertyName': {'native': True, 'name': 'propertyname', 'type': 'string'}, 'defaultValue': {'native': True, 'name': 'defaultvalue', 'type': 'boolean'}})
        self.propertyname = propertyname
        self.defaultvalue = defaultvalue 
