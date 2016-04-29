from .base.ForeignAssetProperty import ForeignAssetPropertyBase
from .actions.ForeignAssetProperty import ForeignAssetPropertyActions

class ForeignAssetProperty(ForeignAssetPropertyBase, ForeignAssetPropertyActions):
    '''
    classdocs
    '''
    def __init__(self, propertydefinitionreference=None):
        '''
        Constructor
        @param propertydefinitionreference: propertydefinitionreference minOccurs=0
        @type propertydefinitionreference: Link
        '''
        ForeignAssetPropertyBase.__init__(self, propertydefinitionreference=propertydefinitionreference)
