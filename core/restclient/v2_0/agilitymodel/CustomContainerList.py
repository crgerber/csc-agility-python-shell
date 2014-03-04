from core.restclient.v2_0.agilitymodel.base.CustomContainerList import CustomContainerListBase
from core.restclient.v2_0.agilitymodel.actions.CustomContainerList import CustomContainerListActions

class CustomContainerList(CustomContainerListBase, CustomContainerListActions):
    '''
    classdocs
    '''
    def __init__(self, customContainer=list()):
        '''
        Constructor
        @param customContainer: customContainer minOccurs=0 maxOccurs=unbounded
        @type customContainer: CustomContainer
        '''
        CustomContainerListBase.__init__(self, customContainer=customContainer)
