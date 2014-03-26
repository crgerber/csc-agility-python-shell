from core.agility.v3_0.agilitymodel.base.FieldMeta import FieldMetaBase
from core.agility.v3_0.agilitymodel.actions.FieldMeta import FieldMetaActions

class FieldMeta(FieldMetaBase, FieldMetaActions):
    '''
    classdocs
    '''
    def __init__(self, displayname='', name=''):
        '''
        Constructor
        @param displayname: displayname
        @type displayname: string
        @param name: name
        @type name: string
        '''
        FieldMetaBase.__init__(self, displayname=displayname, name=name)
