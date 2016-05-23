from core.agility.v3_3.agilitymodel.base.CloudPropertyRequest import CloudPropertyRequestBase
from core.agility.v3_3.agilitymodel.actions.CloudPropertyRequest import CloudPropertyRequestActions

class CloudPropertyRequest(CloudPropertyRequestBase, CloudPropertyRequestActions):
    '''
    classdocs
    '''
    def __init__(self, defaultvalue=False, propertyname=''):
        '''
        Constructor
        @param defaultvalue: defaultvalue
        @type defaultvalue: boolean
        @param propertyname: propertyname
        @type propertyname: string
        '''
        CloudPropertyRequestBase.__init__(self, defaultvalue=defaultvalue, propertyname=propertyname)
