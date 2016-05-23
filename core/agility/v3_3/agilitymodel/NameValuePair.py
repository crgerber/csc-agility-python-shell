from core.agility.v3_3.agilitymodel.base.NameValuePair import NameValuePairBase
from core.agility.v3_3.agilitymodel.actions.NameValuePair import NameValuePairActions

class NameValuePair(NameValuePairBase, NameValuePairActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', value=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param name: name
        @type name: string
        @param value: value minOccurs=0
        @type value: string
        '''
        NameValuePairBase.__init__(self, id=id, name=name, value=value)
