from core.agility.v3_3.agilitymodel.base.StoreResource import StoreResourceBase
from core.agility.v3_3.agilitymodel.actions.StoreResource import StoreResourceActions

class StoreResource(StoreResourceBase, StoreResourceActions):
    '''
    classdocs
    '''
    def __init__(self, name='', value='', id=None, type=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param value: value
        @type value: string
        @param id: id
        @type id: int
        @param type: type
        @type type: string
        '''
        StoreResourceBase.__init__(self, name=name, value=value, id=id, type=type)
