from core.agility.v2_0.agilitymodel.base.Runtime import RuntimeBase
from core.agility.v2_0.agilitymodel.actions.Runtime import RuntimeActions

class Runtime(RuntimeBase, RuntimeActions):
    '''
    classdocs
    '''
    def __init__(self, environment=None, variables=list(), platformService=None, properties=list()):
        '''
        Constructor
        @param environment: environment minOccurs=0
        @type environment: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param platformService: platformService minOccurs=0
        @type platformService: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        RuntimeBase.__init__(self, environment=environment, variables=variables, platformService=platformService, properties=properties)
