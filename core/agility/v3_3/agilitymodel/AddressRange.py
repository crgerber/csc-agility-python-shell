from core.agility.v3_3.agilitymodel.base.AddressRange import AddressRangeBase
from core.agility.v3_3.agilitymodel.actions.AddressRange import AddressRangeActions

class AddressRange(AddressRangeBase, AddressRangeActions):
    '''
    classdocs
    '''
    def __init__(self, network=None, inetmax=None, rangemax=None, rangemin=None, rangetype=None, availableaddresses=[], inetmin=None):
        '''
        Constructor
        @param network: network minOccurs=0
        @type network: Link
        @param inetmax: inetmax minOccurs=0
        @type inetmax: string
        @param rangemax: rangemax minOccurs=0
        @type rangemax: string
        @param rangemin: rangemin minOccurs=0
        @type rangemin: string
        @param rangetype: rangetype minOccurs=0
        @type rangetype: string
        @param availableaddresses: availableaddresses minOccurs=0 maxOccurs=unbounded
        @type availableaddresses: Address
        @param inetmin: inetmin minOccurs=0
        @type inetmin: string
        '''
        AddressRangeBase.__init__(self, network=network, inetmax=inetmax, rangemax=rangemax, rangemin=rangemin, rangetype=rangetype, availableaddresses=availableaddresses, inetmin=inetmin)
