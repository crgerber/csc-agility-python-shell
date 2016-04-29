from core.agility.v3_3.agilitymodel.base.CloudType import CloudTypeBase
from core.agility.v3_3.agilitymodel.actions.CloudType import CloudTypeActions

class CloudType(CloudTypeBase, CloudTypeActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], models=[], type=None):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param models: models minOccurs=0 maxOccurs=unbounded
        @type models: Link
        @param type: type minOccurs=0
        @type type: string
        '''
        CloudTypeBase.__init__(self, properties=properties, models=models, type=type)
