from core.agility.v3_3.agilitymodel.base.RouterInterface import RouterInterfaceBase
from core.agility.v3_3.agilitymodel.actions.RouterInterface import RouterInterfaceActions

class RouterInterface(RouterInterfaceBase, RouterInterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, port=None, subnet=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param port: port minOccurs=0
        @type port: Link
        @param subnet: subnet minOccurs=0
        @type subnet: Link
        '''
        RouterInterfaceBase.__init__(self, id=id, port=port, subnet=subnet)
