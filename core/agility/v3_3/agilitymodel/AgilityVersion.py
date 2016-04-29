from core.agility.v3_3.agilitymodel.base.AgilityVersion import AgilityVersionBase
from core.agility.v3_3.agilitymodel.actions.AgilityVersion import AgilityVersionActions

class AgilityVersion(AgilityVersionBase, AgilityVersionActions):
    '''
    classdocs
    '''
    def __init__(self, build='', version='', url=''):
        '''
        Constructor
        @param build: build
        @type build: string
        @param version: version
        @type version: string
        @param url: url
        @type url: string
        '''
        AgilityVersionBase.__init__(self, build=build, version=version, url=url)
