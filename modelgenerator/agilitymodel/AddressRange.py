from base.AddressRange import AddressRangeBase
from actions.AddressRange import AddressRangeActions

class AddressRange(AddressRangeBase, AddressRangeActions):
    '''
    classdocs
    '''
    def __init__(self, network=None, rangeType=None, inetMax=None, inetMin=None, availableAddresses=list(), rangeMax=None, rangeMin=None):
        '''
        Constructor
        @param network: network minOccurs=0
        @type network: Link
        @param rangeType: rangeType minOccurs=0
        @type rangeType: string
        @param inetMax: inetMax minOccurs=0
        @type inetMax: string
        @param inetMin: inetMin minOccurs=0
        @type inetMin: string
        @param availableAddresses: availableAddresses minOccurs=0 maxOccurs=unbounded
        @type availableAddresses: Address
        @param rangeMax: rangeMax minOccurs=0
        @type rangeMax: string
        @param rangeMin: rangeMin minOccurs=0
        @type rangeMin: string
        '''
        AddressRangeBase.__init__(self, network=network, rangeType=rangeType, inetMax=inetMax, inetMin=inetMin, availableAddresses=availableAddresses, rangeMax=rangeMax, rangeMin=rangeMin)
