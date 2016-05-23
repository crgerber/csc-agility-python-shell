from core.agility.v3_3.agilitymodel.base.StorePrice import StorePriceBase
from core.agility.v3_3.agilitymodel.actions.StorePrice import StorePriceActions

class StorePrice(StorePriceBase, StorePriceActions):
    '''
    classdocs
    '''
    def __init__(self, duration=None, labelafter=None, digits=None, label=None, currencylabel=None, id=None, period=None, price=None, threshold=None, recurs=None, type=None, currency=None):
        '''
        Constructor
        @param duration: duration minOccurs=0
        @type duration: int
        @param labelafter: labelafter minOccurs=0
        @type labelafter: boolean
        @param digits: digits minOccurs=0
        @type digits: int
        @param label: label minOccurs=0
        @type label: string
        @param currencylabel: currencylabel minOccurs=0
        @type currencylabel: string
        @param id: id minOccurs=0
        @type id: int
        @param period: period minOccurs=0
        @type period: int
        @param price: price minOccurs=0
        @type price: double
        @param threshold: threshold minOccurs=0
        @type threshold: double
        @param recurs: recurs minOccurs=0
        @type recurs: int
        @param type: type minOccurs=0
        @type type: string
        @param currency: currency minOccurs=0
        @type currency: string
        '''
        StorePriceBase.__init__(self, duration=duration, labelafter=labelafter, digits=digits, label=label, currencylabel=currencylabel, id=id, period=period, price=price, threshold=threshold, recurs=recurs, type=type, currency=currency)
