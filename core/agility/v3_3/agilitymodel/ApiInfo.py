from core.agility.v3_3.agilitymodel.base.ApiInfo import ApiInfoBase
from core.agility.v3_3.agilitymodel.actions.ApiInfo import ApiInfoActions

class ApiInfo(ApiInfoBase, ApiInfoActions):
    '''
    classdocs
    '''
    def __init__(self, realpath=None, path=None, apiname=None, version=None):
        '''
        Constructor
        @param realpath: realpath minOccurs=0
        @type realpath: string
        @param path: path minOccurs=0
        @type path: string
        @param apiname: apiname minOccurs=0
        @type apiname: string
        @param version: version minOccurs=0
        @type version: string
        '''
        ApiInfoBase.__init__(self, realpath=realpath, path=path, apiname=apiname, version=version)
