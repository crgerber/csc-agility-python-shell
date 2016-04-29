from .base.StoreResource import StoreResourceBase
from .actions.StoreResource import StoreResourceActions

class StoreResource(StoreResourceBase, StoreResourceActions):
    '''
    classdocs
    '''
    def __init__(self, type='', id=None, value='', name=''):
        '''
        Constructor
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        @param value: value
        @type value: string
        @param name: name
        @type name: string
        '''
        StoreResourceBase.__init__(self, type=type, id=id, value=value, name=name)
