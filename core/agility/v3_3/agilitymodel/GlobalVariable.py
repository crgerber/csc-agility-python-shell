from base.GlobalVariable import GlobalVariableBase
from actions.GlobalVariable import GlobalVariableActions

class GlobalVariable(GlobalVariableBase, GlobalVariableActions):
    '''
    classdocs
    '''
    def __init__(self, key='', floatvalue=None, doublevalue=None, intvalue=None, datevalue=None, bytevalue=None, stringvalue=None, booleanvalue=None):
        '''
        Constructor
        @param key: key
        @type key: string
        @param floatvalue: floatvalue minOccurs=0
        @type floatvalue: float
        @param doublevalue: doublevalue minOccurs=0
        @type doublevalue: double
        @param intvalue: intvalue minOccurs=0
        @type intvalue: int
        @param datevalue: datevalue minOccurs=0
        @type datevalue: date
        @param bytevalue: bytevalue minOccurs=0
        @type bytevalue: hexBinary
        @param stringvalue: stringvalue minOccurs=0
        @type stringvalue: string
        @param booleanvalue: booleanvalue minOccurs=0
        @type booleanvalue: boolean
        '''
        GlobalVariableBase.__init__(self, key=key, floatvalue=floatvalue, doublevalue=doublevalue, intvalue=intvalue, datevalue=datevalue, bytevalue=bytevalue, stringvalue=stringvalue, booleanvalue=booleanvalue)
