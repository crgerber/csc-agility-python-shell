from core.restclient.v2_0.agilitymodel.base.StorePublisher import StorePublisherBase
from core.restclient.v2_0.agilitymodel.actions.StorePublisher import StorePublisherActions

class StorePublisher(StorePublisherBase, StorePublisherActions):
    '''
    classdocs
    '''
    def __init__(self, url=None):
        '''
        Constructor
        @param url: url minOccurs=0
        @type url: string
        '''
        StorePublisherBase.__init__(self, url=url)
