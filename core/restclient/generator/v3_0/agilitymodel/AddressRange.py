from base.AddressRange import AddressRangeBase
from actions.AddressRange import AddressRangeActions

class AddressRange(AddressRangeBase, AddressRangeActions):
    '''
    classdocs
    '''
    def __init__(self, network=None, rangetype=None, inetmax=None, inetmin=None, availableaddresses=[], rangemax=None, rangemin=None):
        '''
        Constructor
        @param network: network minOccurs=0
        @type network: Link
        @param rangetype: rangetype minOccurs=0
        @type rangetype: string
        @param inetmax: inetmax minOccurs=0
        @type inetmax: string
        @param inetmin: inetmin minOccurs=0
        @type inetmin: string
        @param availableaddresses: availableaddresses minOccurs=0 maxOccurs=unbounded
        @type availableaddresses: Address
        @param rangemax: rangemax minOccurs=0
        @type rangemax: string
        @param rangemin: rangemin minOccurs=0
        @type rangemin: string
        '''
        AddressRangeBase.__init__(self, network=network, rangetype=rangetype, inetmax=inetmax, inetmin=inetmin, availableaddresses=availableaddresses, rangemax=rangemax, rangemin=rangemin)
