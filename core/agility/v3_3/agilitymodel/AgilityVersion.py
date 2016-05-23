from core.agility.v3_3.agilitymodel.base.AgilityVersion import AgilityVersionBase
from core.agility.v3_3.agilitymodel.actions.AgilityVersion import AgilityVersionActions

class AgilityVersion(AgilityVersionBase, AgilityVersionActions):
    '''
    classdocs
    '''
    def __init__(self, build='', url='', version=''):
        '''
        Constructor
        @param build: build
        @type build: string
        @param url: url
        @type url: string
        @param version: version
        @type version: string
        '''
        AgilityVersionBase.__init__(self, build=build, url=url, version=version)
