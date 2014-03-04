from core.restclient.v2_0.agilitymodel.base.CloudType import CloudTypeBase
from core.restclient.v2_0.agilitymodel.actions.CloudType import CloudTypeActions

class CloudType(CloudTypeBase, CloudTypeActions):
    '''
    classdocs
    '''
    def __init__(self, models=list(), type=None, properties=list()):
        '''
        Constructor
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        @param type: type minOccurs=0
        @type type: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        CloudTypeBase.__init__(self, models=models, type=type, properties=properties)
