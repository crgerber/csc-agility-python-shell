from core.agility.v3_3.agilitymodel.base.GlobalVariable import GlobalVariableBase
from core.agility.v3_3.agilitymodel.actions.GlobalVariable import GlobalVariableActions

class GlobalVariable(GlobalVariableBase, GlobalVariableActions):
    '''
    classdocs
    '''
    def __init__(self, booleanvalue=None, doublevalue=None, floatvalue=None, stringvalue=None, bytevalue=None, datevalue=None, key='', intvalue=None):
        '''
        Constructor
        @param booleanvalue: booleanvalue minOccurs=0
        @type booleanvalue: boolean
        @param doublevalue: doublevalue minOccurs=0
        @type doublevalue: double
        @param floatvalue: floatvalue minOccurs=0
        @type floatvalue: float
        @param stringvalue: stringvalue minOccurs=0
        @type stringvalue: string
        @param bytevalue: bytevalue minOccurs=0
        @type bytevalue: hexBinary
        @param datevalue: datevalue minOccurs=0
        @type datevalue: date
        @param key: key
        @type key: string
        @param intvalue: intvalue minOccurs=0
        @type intvalue: int
        '''
        GlobalVariableBase.__init__(self, booleanvalue=booleanvalue, doublevalue=doublevalue, floatvalue=floatvalue, stringvalue=stringvalue, bytevalue=bytevalue, datevalue=datevalue, key=key, intvalue=intvalue)
