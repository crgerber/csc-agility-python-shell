from CreateRequest import CreateRequestBase

class UpdateRequestBase(CreateRequestBase):
    '''
    classdocs
    '''
    def __init__(self):
        CreateRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
