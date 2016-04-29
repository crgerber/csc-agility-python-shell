from core.agility.v3_3.agilitymodel.base.ApiInfo import ApiInfoBase
from core.agility.v3_3.agilitymodel.actions.ApiInfo import ApiInfoActions

class ApiInfo(ApiInfoBase, ApiInfoActions):
    '''
    classdocs
    '''
    def __init__(self, path=None, realpath=None, version=None, apiname=None):
        '''
        Constructor
        @param path: path minOccurs=0
        @type path: string
        @param realpath: realpath minOccurs=0
        @type realpath: string
        @param version: version minOccurs=0
        @type version: string
        @param apiname: apiname minOccurs=0
        @type apiname: string
        '''
        ApiInfoBase.__init__(self, path=path, realpath=realpath, version=version, apiname=apiname)
