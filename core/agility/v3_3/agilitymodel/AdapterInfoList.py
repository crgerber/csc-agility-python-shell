from core.agility.v3_3.agilitymodel.base.AdapterInfoList import AdapterInfoListBase
from core.agility.v3_3.agilitymodel.actions.AdapterInfoList import AdapterInfoListActions

class AdapterInfoList(AdapterInfoListBase, AdapterInfoListActions):
    '''
    classdocs
    '''
    def __init__(self, adapterinfo=[]):
        '''
        Constructor
        @param adapterinfo: adapterinfo minOccurs=0 maxOccurs=unbounded
        @type adapterinfo: AdapterInfo
        '''
        AdapterInfoListBase.__init__(self, adapterinfo=adapterinfo)
