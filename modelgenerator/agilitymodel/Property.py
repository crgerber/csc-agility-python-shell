from base.Property import PropertyBase
from actions.Property import PropertyActions

class Property(PropertyBase, PropertyActions):
    '''
    classdocs
    '''
    def __init__(self, availableOptions=list(), encrypted=False, overridable=False, value='', data=None, dataEncrypted=False):
        '''
        Constructor
        @param availableOptions: availableOptions minOccurs=0 maxOccurs=unbounded
        @type availableOptions: string
        @param encrypted: encrypted
        @type encrypted: boolean
        @param overridable: overridable
        @type overridable: boolean
        @param value: value
        @type value: string
        @param data: data minOccurs=0
        @type data: hexBinary
        @param dataEncrypted: dataEncrypted
        @type dataEncrypted: boolean
        '''
        PropertyBase.__init__(self, availableOptions=availableOptions, encrypted=encrypted, overridable=overridable, value=value, data=data, dataEncrypted=dataEncrypted)
