from core.agility.v3_3.agilitymodel.base.AgilityVersion import AgilityVersionBase
from core.agility.v3_3.agilitymodel.actions.AgilityVersion import AgilityVersionActions

class AgilityVersion(AgilityVersionBase, AgilityVersionActions):
    '''
    classdocs
    '''
    def __init__(self, url='', version='', build=''):
        '''
        Constructor
        @param url: url
        @type url: string
        @param version: version
        @type version: string
        @param build: build
        @type build: string
        '''
        AgilityVersionBase.__init__(self, url=url, version=version, build=build)
