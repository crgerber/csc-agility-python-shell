from core.agility.v3_0.agilitymodel.base.ScriptVariableRequest import ScriptVariableRequestBase
from core.agility.v3_0.agilitymodel.actions.ScriptVariableRequest import ScriptVariableRequestActions

class ScriptVariableRequest(ScriptVariableRequestBase, ScriptVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, topologyid=None, cloudid=[], packageid=[], templateid=None):
        '''
        Constructor
        @param topologyid: topologyid minOccurs=0
        @type topologyid: int
        @param cloudid: cloudid minOccurs=0 maxOccurs=unbounded
        @type cloudid: int
        @param packageid: packageid minOccurs=0 maxOccurs=unbounded
        @type packageid: int
        @param templateid: templateid minOccurs=0
        @type templateid: int
        '''
        ScriptVariableRequestBase.__init__(self, topologyid=topologyid, cloudid=cloudid, packageid=packageid, templateid=templateid)
