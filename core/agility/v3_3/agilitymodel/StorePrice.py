from core.agility.v3_3.agilitymodel.base.StorePrice import StorePriceBase
from core.agility.v3_3.agilitymodel.actions.StorePrice import StorePriceActions

class StorePrice(StorePriceBase, StorePriceActions):
    '''
    classdocs
    '''
    def __init__(self, currency=None, recurs=None, label=None, digits=None, id=None, period=None, threshold=None, currencylabel=None, labelafter=None, price=None, duration=None, type=None):
        '''
        Constructor
        @param currency: currency minOccurs=0
        @type currency: string
        @param recurs: recurs minOccurs=0
        @type recurs: int
        @param label: label minOccurs=0
        @type label: string
        @param digits: digits minOccurs=0
        @type digits: int
        @param id: id minOccurs=0
        @type id: int
        @param period: period minOccurs=0
        @type period: int
        @param threshold: threshold minOccurs=0
        @type threshold: double
        @param currencylabel: currencylabel minOccurs=0
        @type currencylabel: string
        @param labelafter: labelafter minOccurs=0
        @type labelafter: boolean
        @param price: price minOccurs=0
        @type price: double
        @param duration: duration minOccurs=0
        @type duration: int
        @param type: type minOccurs=0
        @type type: string
        '''
        StorePriceBase.__init__(self, currency=currency, recurs=recurs, label=label, digits=digits, id=id, period=period, threshold=threshold, currencylabel=currencylabel, labelafter=labelafter, price=price, duration=duration, type=type)
