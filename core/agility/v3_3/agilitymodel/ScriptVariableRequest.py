from core.agility.v3_3.agilitymodel.base.ScriptVariableRequest import ScriptVariableRequestBase
from core.agility.v3_3.agilitymodel.actions.ScriptVariableRequest import ScriptVariableRequestActions

class ScriptVariableRequest(ScriptVariableRequestBase, ScriptVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, templateid=None, cloudid=[], topologyid=None, packageid=[]):
        '''
        Constructor
        @param templateid: templateid minOccurs=0
        @type templateid: int
        @param cloudid: cloudid minOccurs=0 maxOccurs=unbounded
        @type cloudid: int
        @param topologyid: topologyid minOccurs=0
        @type topologyid: int
        @param packageid: packageid minOccurs=0 maxOccurs=unbounded
        @type packageid: int
        '''
        ScriptVariableRequestBase.__init__(self, templateid=templateid, cloudid=cloudid, topologyid=topologyid, packageid=packageid)
