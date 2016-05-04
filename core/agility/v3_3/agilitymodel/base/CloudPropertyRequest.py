from ApiRequest import ApiRequestBase

class CloudPropertyRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, propertyname='', defaultvalue=False):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'propertyName': {'type': 'string', 'name': 'propertyname', 'native': True}, 'defaultValue': {'type': 'boolean', 'name': 'defaultvalue', 'native': True}})
        self.propertyname = propertyname
        self.defaultvalue = defaultvalue 
