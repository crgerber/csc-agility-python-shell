from core.agility.v3_3.agilitymodel.base.ErrorMessage import ErrorMessageBase
from core.agility.v3_3.agilitymodel.actions.ErrorMessage import ErrorMessageActions

class ErrorMessage(ErrorMessageBase, ErrorMessageActions):
    '''
    classdocs
    '''
    def __init__(self, message='', code='', iserror=False, detail=''):
        '''
        Constructor
        @param message: message
        @type message: string
        @param code: code
        @type code: string
        @param iserror: iserror
        @type iserror: boolean
        @param detail: detail
        @type detail: string
        '''
        ErrorMessageBase.__init__(self, message=message, code=code, iserror=iserror, detail=detail)
