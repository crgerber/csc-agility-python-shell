from core.agility.v3_3.agilitymodel.base.GlobalVariable import GlobalVariableBase
from core.agility.v3_3.agilitymodel.actions.GlobalVariable import GlobalVariableActions

class GlobalVariable(GlobalVariableBase, GlobalVariableActions):
    '''
    classdocs
    '''
    def __init__(self, datevalue=None, stringvalue=None, doublevalue=None, booleanvalue=None, intvalue=None, key=None, bytevalue=None, floatvalue=None):
        '''
        Constructor
        @param datevalue: datevalue minOccurs=0
        @type datevalue: date
        @param stringvalue: stringvalue minOccurs=0
        @type stringvalue: string
        @param doublevalue: doublevalue minOccurs=0
        @type doublevalue: double
        @param booleanvalue: booleanvalue minOccurs=0
        @type booleanvalue: boolean
        @param intvalue: intvalue minOccurs=0
        @type intvalue: int
        @param key: key minOccurs=0
        @type key: string
        @param bytevalue: bytevalue minOccurs=0
        @type bytevalue: hexBinary
        @param floatvalue: floatvalue minOccurs=0
        @type floatvalue: float
        '''
        GlobalVariableBase.__init__(self, datevalue=datevalue, stringvalue=stringvalue, doublevalue=doublevalue, booleanvalue=booleanvalue, intvalue=intvalue, key=key, bytevalue=bytevalue, floatvalue=floatvalue)
