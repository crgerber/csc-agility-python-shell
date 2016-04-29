from core.agility.v3_3.agilitymodel.base.Runtime import RuntimeBase
from core.agility.v3_3.agilitymodel.actions.Runtime import RuntimeActions

class Runtime(RuntimeBase, RuntimeActions):
    '''
    classdocs
    '''
    def __init__(self, platformservice=None, variables=[], environment=None, properties=[]):
        '''
        Constructor
        @param platformservice: platformservice minOccurs=0
        @type platformservice: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param environment: environment minOccurs=0
        @type environment: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        RuntimeBase.__init__(self, platformservice=platformservice, variables=variables, environment=environment, properties=properties)
