from core.agility.v3_0.agilitymodel.base.StorePrice import StorePriceBase
from core.agility.v3_0.agilitymodel.actions.StorePrice import StorePriceActions

class StorePrice(StorePriceBase, StorePriceActions):
    '''
    classdocs
    '''
    def __init__(self, digits=None, labelafter=None, recurs=None, currencylabel=None, price=None, period=None, label=None, currency=None, threshold=None, duration=None, type=None, id=None):
        '''
        Constructor
        @param digits: digits minOccurs=0
        @type digits: int
        @param labelafter: labelafter minOccurs=0
        @type labelafter: boolean
        @param recurs: recurs minOccurs=0
        @type recurs: int
        @param currencylabel: currencylabel minOccurs=0
        @type currencylabel: string
        @param price: price minOccurs=0
        @type price: double
        @param period: period minOccurs=0
        @type period: int
        @param label: label minOccurs=0
        @type label: string
        @param currency: currency minOccurs=0
        @type currency: string
        @param threshold: threshold minOccurs=0
        @type threshold: double
        @param duration: duration minOccurs=0
        @type duration: int
        @param type: type minOccurs=0
        @type type: string
        @param id: id minOccurs=0
        @type id: int
        '''
        StorePriceBase.__init__(self, digits=digits, labelafter=labelafter, recurs=recurs, currencylabel=currencylabel, price=price, period=period, label=label, currency=currency, threshold=threshold, duration=duration, type=type, id=id)
