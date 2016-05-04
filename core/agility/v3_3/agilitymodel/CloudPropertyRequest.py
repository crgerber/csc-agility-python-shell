from base.CloudPropertyRequest import CloudPropertyRequestBase
from actions.CloudPropertyRequest import CloudPropertyRequestActions

class CloudPropertyRequest(CloudPropertyRequestBase, CloudPropertyRequestActions):
    '''
    classdocs
    '''
    def __init__(self, propertyname='', defaultvalue=False):
        '''
        Constructor
        @param propertyname: propertyname
        @type propertyname: string
        @param defaultvalue: defaultvalue
        @type defaultvalue: boolean
        '''
        CloudPropertyRequestBase.__init__(self, propertyname=propertyname, defaultvalue=defaultvalue)
