from base.FieldMeta import FieldMetaBase
from actions.FieldMeta import FieldMetaActions

class FieldMeta(FieldMetaBase, FieldMetaActions):
    '''
    classdocs
    '''
    def __init__(self, displayName='', name=''):
        '''
        Constructor
        @param displayName: displayName
        @type displayName: string
        @param name: name
        @type name: string
        '''
        FieldMetaBase.__init__(self, displayName=displayName, name=name)
