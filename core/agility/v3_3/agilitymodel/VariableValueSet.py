from core.agility.v3_3.agilitymodel.base.VariableValueSet import VariableValueSetBase
from core.agility.v3_3.agilitymodel.actions.VariableValueSet import VariableValueSetActions

class VariableValueSet(VariableValueSetBase, VariableValueSetActions):
    '''
    classdocs
    '''
    def __init__(self, valuesource=None, value=[]):
        '''
        Constructor
        @param valuesource: valuesource minOccurs=0
        @type valuesource: Asset
        @param value: value minOccurs=0 maxOccurs=unbounded
        @type value: AssetProperty
        '''
        VariableValueSetBase.__init__(self, valuesource=valuesource, value=value)
