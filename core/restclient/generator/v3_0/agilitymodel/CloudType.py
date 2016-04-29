from .base.CloudType import CloudTypeBase
from .actions.CloudType import CloudTypeActions

class CloudType(CloudTypeBase, CloudTypeActions):
    '''
    classdocs
    '''
    def __init__(self, models=[], type=None, properties=[]):
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
