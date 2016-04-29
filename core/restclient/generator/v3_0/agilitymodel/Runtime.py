from .base.Runtime import RuntimeBase
from .actions.Runtime import RuntimeActions

class Runtime(RuntimeBase, RuntimeActions):
    '''
    classdocs
    '''
    def __init__(self, environment=None, variables=[], platformservice=None, properties=[]):
        '''
        Constructor
        @param environment: environment minOccurs=0
        @type environment: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param platformservice: platformservice minOccurs=0
        @type platformservice: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        RuntimeBase.__init__(self, environment=environment, variables=variables, platformservice=platformservice, properties=properties)
