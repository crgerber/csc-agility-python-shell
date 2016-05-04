from base.ApiInfo import ApiInfoBase
from actions.ApiInfo import ApiInfoActions

class ApiInfo(ApiInfoBase, ApiInfoActions):
    '''
    classdocs
    '''
    def __init__(self, realpath=None, version=None, apiname=None, path=None):
        '''
        Constructor
        @param realpath: realpath minOccurs=0
        @type realpath: string
        @param version: version minOccurs=0
        @type version: string
        @param apiname: apiname minOccurs=0
        @type apiname: string
        @param path: path minOccurs=0
        @type path: string
        '''
        ApiInfoBase.__init__(self, realpath=realpath, version=version, apiname=apiname, path=path)
