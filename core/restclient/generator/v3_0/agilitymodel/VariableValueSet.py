from .base.VariableValueSet import VariableValueSetBase
from .actions.VariableValueSet import VariableValueSetActions

class VariableValueSet(VariableValueSetBase, VariableValueSetActions):
    '''
    classdocs
    '''
    def __init__(self, value=[], valuesource=None):
        '''
        Constructor
        @param value: value minOccurs=0 maxOccurs=unbounded
        @type value: AssetProperty
        @param valuesource: valuesource minOccurs=0
        @type valuesource: Asset
        '''
        VariableValueSetBase.__init__(self, value=value, valuesource=valuesource)
