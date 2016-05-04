from base.Baselink import BaselinkBase
from actions.Baselink import BaselinkActions

class Baselink(BaselinkBase, BaselinkActions):
    '''
    classdocs
    '''
    def __init__(self, href=None, name=None):
        '''
        Constructor
        @param href: href minOccurs=0
        @type href: string
        @param name: name minOccurs=0
        @type name: string
        '''
        BaselinkBase.__init__(self, href=href, name=name)
