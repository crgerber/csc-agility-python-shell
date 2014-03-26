from core.agility.v3_0.agilitymodel.base.ForeignAssetProperty import ForeignAssetPropertyBase
from core.agility.v3_0.agilitymodel.actions.ForeignAssetProperty import ForeignAssetPropertyActions

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
