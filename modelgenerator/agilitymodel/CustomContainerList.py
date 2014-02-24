from base.CustomContainerList import CustomContainerListBase
from actions.CustomContainerList import CustomContainerListActions

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
