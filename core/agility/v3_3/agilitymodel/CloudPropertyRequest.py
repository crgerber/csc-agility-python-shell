from core.agility.v3_3.agilitymodel.base.CloudPropertyRequest import CloudPropertyRequestBase
from core.agility.v3_3.agilitymodel.actions.CloudPropertyRequest import CloudPropertyRequestActions

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
