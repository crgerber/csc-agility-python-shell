from .base.ObjectReference import ObjectReferenceBase
from .actions.ObjectReference import ObjectReferenceActions

class ObjectReference(ObjectReferenceBase, ObjectReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, fieldname=None, fieldassettypename=None):
        '''
        Constructor
        @param fieldname: fieldname minOccurs=0
        @type fieldname: string
        @param fieldassettypename: fieldassettypename minOccurs=0
        @type fieldassettypename: string
        '''
        ObjectReferenceBase.__init__(self, fieldname=fieldname, fieldassettypename=fieldassettypename)
