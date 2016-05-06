from core.agility.v3_3.agilitymodel.base.RouterInterface import RouterInterfaceBase
from core.agility.v3_3.agilitymodel.actions.RouterInterface import RouterInterfaceActions

class RouterInterface(RouterInterfaceBase, RouterInterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, subnet=None, id=None, port=None):
        '''
        Constructor
        @param subnet: subnet minOccurs=0
        @type subnet: Link
        @param id: id minOccurs=0
        @type id: int
        @param port: port minOccurs=0
        @type port: Link
        '''
        RouterInterfaceBase.__init__(self, subnet=subnet, id=id, port=port)
