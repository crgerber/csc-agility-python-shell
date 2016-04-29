from core.agility.v3_3.agilitymodel.base.FieldMeta import FieldMetaBase
from core.agility.v3_3.agilitymodel.actions.FieldMeta import FieldMetaActions

class FieldMeta(FieldMetaBase, FieldMetaActions):
    '''
    classdocs
    '''
    def __init__(self, name='', displayname=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param displayname: displayname
        @type displayname: string
        '''
        FieldMetaBase.__init__(self, name=name, displayname=displayname)
