from core.agility.v3_0.agilitymodel.base.ScriptClasspath import ScriptClasspathBase
from core.agility.v3_0.agilitymodel.actions.ScriptClasspath import ScriptClasspathActions

class ScriptClasspath(ScriptClasspathBase, ScriptClasspathActions):
    '''
    classdocs
    '''
    def __init__(self, path='', unerasable=False, domain=None):
        '''
        Constructor
        @param path: path
        @type path: string
        @param unerasable: unerasable
        @type unerasable: boolean
        @param domain: domain minOccurs=0
        @type domain: Link
        '''
        ScriptClasspathBase.__init__(self, path=path, unerasable=unerasable, domain=domain)
