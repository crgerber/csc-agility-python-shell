from core.agility.v3_3.agilitymodel.base.StoreResource import StoreResourceBase
from core.agility.v3_3.agilitymodel.actions.StoreResource import StoreResourceActions

class StoreResource(StoreResourceBase, StoreResourceActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', value='', type=''):
        '''
        Constructor
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        @param value: value
        @type value: string
        @param type: type
        @type type: string
        '''
        StoreResourceBase.__init__(self, id=id, name=name, value=value, type=type)
