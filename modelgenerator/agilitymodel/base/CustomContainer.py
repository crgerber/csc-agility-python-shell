from Container import ContainerBase

class CustomContainerBase(ContainerBase):
    '''
    classdocs
    '''
    def __init__(self):
        ContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
