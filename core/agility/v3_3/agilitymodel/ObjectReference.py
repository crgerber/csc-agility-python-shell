from core.agility.v3_3.agilitymodel.base.ObjectReference import ObjectReferenceBase
from core.agility.v3_3.agilitymodel.actions.ObjectReference import ObjectReferenceActions

class ObjectReference(ObjectReferenceBase, ObjectReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, fieldassettypename=None, fieldname=None):
        '''
        Constructor
        @param fieldassettypename: fieldassettypename minOccurs=0
        @type fieldassettypename: string
        @param fieldname: fieldname minOccurs=0
        @type fieldname: string
        '''
        ObjectReferenceBase.__init__(self, fieldassettypename=fieldassettypename, fieldname=fieldname)
