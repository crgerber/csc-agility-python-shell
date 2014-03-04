from core.restclient.v2_0.agilitymodel.base.AddressRangeList import AddressRangeListBase
from core.restclient.v2_0.agilitymodel.actions.AddressRangeList import AddressRangeListActions

class AddressRangeList(AddressRangeListBase, AddressRangeListActions):
    '''
    classdocs
    '''
    def __init__(self, AddressRange=list()):
        '''
        Constructor
        @param AddressRange: AddressRange minOccurs=0 maxOccurs=unbounded
        @type AddressRange: AddressRange
        '''
        AddressRangeListBase.__init__(self, AddressRange=AddressRange)
