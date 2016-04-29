from core.agility.v3_3.agilitymodel.base.Property import PropertyBase
from core.agility.v3_3.agilitymodel.actions.Property import PropertyActions

class Property(PropertyBase, PropertyActions):
    '''
    classdocs
    '''
    def __init__(self, encrypted=False, dataencrypted=False, overridable=False, value='', data=None, availableoptions=[]):
        '''
        Constructor
        @param encrypted: encrypted
        @type encrypted: boolean
        @param dataencrypted: dataencrypted
        @type dataencrypted: boolean
        @param overridable: overridable
        @type overridable: boolean
        @param value: value
        @type value: string
        @param data: data minOccurs=0
        @type data: hexBinary
        @param availableoptions: availableoptions minOccurs=0 maxOccurs=unbounded
        @type availableoptions: string
        '''
        PropertyBase.__init__(self, encrypted=encrypted, dataencrypted=dataencrypted, overridable=overridable, value=value, data=data, availableoptions=availableoptions)
