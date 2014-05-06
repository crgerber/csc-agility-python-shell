from core.agility.v3_0.agilitymodel.base.ErrorMessage import ErrorMessageBase
from core.agility.v3_0.agilitymodel.actions.ErrorMessage import ErrorMessageActions

class ErrorMessage(ErrorMessageBase, ErrorMessageActions):
    '''
    classdocs
    '''
    def __init__(self, message='', code='', detail='', iserror=False):
        '''
        Constructor
        @param message: message
        @type message: string
        @param code: code
        @type code: string
        @param detail: detail
        @type detail: string
        @param iserror: iserror
        @type iserror: boolean
        '''
        ErrorMessageBase.__init__(self, message=message, code=code, detail=detail, iserror=iserror)
