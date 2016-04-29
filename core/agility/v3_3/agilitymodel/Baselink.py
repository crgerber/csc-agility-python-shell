from core.agility.v3_3.agilitymodel.base.Baselink import BaselinkBase
from core.agility.v3_3.agilitymodel.actions.Baselink import BaselinkActions

class Baselink(BaselinkBase, BaselinkActions):
    '''
    classdocs
    '''
    def __init__(self, name=None, href=None):
        '''
        Constructor
        @param name: name minOccurs=0
        @type name: string
        @param href: href minOccurs=0
        @type href: string
        '''
        BaselinkBase.__init__(self, name=name, href=href)
