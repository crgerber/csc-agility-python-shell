from core.agility.v3_3.agilitymodel.base.Property import PropertyBase
from core.agility.v3_3.agilitymodel.actions.Property import PropertyActions

class Property(PropertyBase, PropertyActions):
    '''
    classdocs
    '''
    def __init__(self, value='', data=None, dataencrypted=False, encrypted=False, overridable=False, availableoptions=[]):
        '''
        Constructor
        @param value: value
        @type value: string
        @param data: data minOccurs=0
        @type data: hexBinary
        @param dataencrypted: dataencrypted
        @type dataencrypted: boolean
        @param encrypted: encrypted
        @type encrypted: boolean
        @param overridable: overridable
        @type overridable: boolean
        @param availableoptions: availableoptions minOccurs=0 maxOccurs=unbounded
        @type availableoptions: string
        '''
        PropertyBase.__init__(self, value=value, data=data, dataencrypted=dataencrypted, encrypted=encrypted, overridable=overridable, availableoptions=availableoptions)
