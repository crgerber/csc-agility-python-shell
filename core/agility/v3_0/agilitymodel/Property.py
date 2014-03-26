from core.agility.v3_0.agilitymodel.base.Property import PropertyBase
from core.agility.v3_0.agilitymodel.actions.Property import PropertyActions

class Property(PropertyBase, PropertyActions):
    '''
    classdocs
    '''
    def __init__(self, availableoptions=[], encrypted=False, overridable=False, value='', data=None, dataencrypted=False):
        '''
        Constructor
        @param availableoptions: availableoptions minOccurs=0 maxOccurs=unbounded
        @type availableoptions: string
        @param encrypted: encrypted
        @type encrypted: boolean
        @param overridable: overridable
        @type overridable: boolean
        @param value: value
        @type value: string
        @param data: data minOccurs=0
        @type data: hexBinary
        @param dataencrypted: dataencrypted
        @type dataencrypted: boolean
        '''
        PropertyBase.__init__(self, availableoptions=availableoptions, encrypted=encrypted, overridable=overridable, value=value, data=data, dataencrypted=dataencrypted)
