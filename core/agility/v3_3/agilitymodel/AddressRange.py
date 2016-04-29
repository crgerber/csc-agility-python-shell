from core.agility.v3_3.agilitymodel.base.AddressRange import AddressRangeBase
from core.agility.v3_3.agilitymodel.actions.AddressRange import AddressRangeActions

class AddressRange(AddressRangeBase, AddressRangeActions):
    '''
    classdocs
    '''
    def __init__(self, network=None, rangemin=None, inetmin=None, rangetype=None, inetmax=None, availableaddresses=[], rangemax=None):
        '''
        Constructor
        @param network: network minOccurs=0
        @type network: Link
        @param rangemin: rangemin minOccurs=0
        @type rangemin: string
        @param inetmin: inetmin minOccurs=0
        @type inetmin: string
        @param rangetype: rangetype minOccurs=0
        @type rangetype: string
        @param inetmax: inetmax minOccurs=0
        @type inetmax: string
        @param availableaddresses: availableaddresses minOccurs=0 maxOccurs=unbounded
        @type availableaddresses: Address
        @param rangemax: rangemax minOccurs=0
        @type rangemax: string
        '''
        AddressRangeBase.__init__(self, network=network, rangemin=rangemin, inetmin=inetmin, rangetype=rangetype, inetmax=inetmax, availableaddresses=availableaddresses, rangemax=rangemax)
